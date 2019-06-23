from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

from accounts.models import UserProfile
from bookmark.forms import ListForm, ItemForm
from bookmark.models import BookmarkItem, BookmarkList


class BookmarkListView(ListView):
    model = BookmarkList
    template_name = "bookmark/bookmark_list.html"
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = BookmarkList.objects.filter(user=self.request.user)
            return queryset
        else:
            # TODO: 임시 방편
            return []


class ListCreateView(LoginRequiredMixin, CreateView): # ToDo: login success로 redirect
    model = BookmarkList
    template_name = 'bookmark/list_add.html'
    form_class = ListForm
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        _is_valid = super(ListCreateView, self).form_valid(form)
        if _is_valid:
            _list = form.instance
            _list.user.set([self.request.user])

        return _is_valid


class ListUpdateView(LoginRequiredMixin, UpdateView):
    model = BookmarkList
    template_name = 'bookmark/list_update.html'
    form_class = ListForm
    success_url = reverse_lazy('bookmark:index')


class ListDeleteView(LoginRequiredMixin, DeleteView):
    model=BookmarkList,
    success_url=reverse_lazy('bookmark:index'),
    template_name='bookmark/list_confirm_delete.html',


class ItemListView(ListView):
    model = BookmarkItem
    template_name = "bookmark/item_list.html"
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = BookmarkItem.objects.filter(belonged_list=self.kwargs['pk'])
            return queryset
        else:
            # TODO: 임시 방편
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_list_pk'] = self.kwargs.get('pk')
        return context


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = BookmarkItem
    template_name = 'bookmark/item_add.html'
    form_class = ItemForm

    def get_success_url(self):
        return reverse_lazy(
            'bookmark:item_list',
            args=[self.kwargs.get('pk')],
        )

    def form_valid(self, form):
        list_pk = self.kwargs.get('pk')
        form.instance.belonged_list = BookmarkList.objects.get(pk=list_pk)
        return super(ItemCreateView, self).form_valid(form)


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = BookmarkItem
    template_name = 'bookmark/item_detail.html'


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = BookmarkItem
    template_name = 'bookmark/item_update.html'
    form_class = ItemForm

    def get_success_url(self):
        return reverse_lazy(
            'bookmark:item_list',
            args=[self.kwargs.get('pk')],
        )


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = BookmarkItem
    template_name = 'bookmark/item_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy(
            'bookmark:item_list',
            args=[self.kwargs.get('list_pk')],
        )


class PublicBookmarkListView(ListView):
    model = BookmarkList
    template_name = "bookmark/public_bookmark_list.html"
    paginate_by = 6

    def get_queryset(self):
        _user = UserProfile.objects.filter(nickname=self.kwargs.get('nickname')).get()
        print(_user)
        if _user:
            queryset = get_list_or_404(BookmarkList, user=_user, access_level='S')
            return queryset
        else:
            # TODO: 임시 방편
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_nickname'] = self.kwargs.get('nickname')

        _user = self.request.user
        _list = context['object_list']

        _is_list_fan = dict()
        for item in _list:
            _is_list_fan[item.pk] = _user.is_list_fan(item.pk)

        print(_is_list_fan)

        context['is_fan'] = _is_list_fan

        return context


class PublicItemListView(ListView):
    model = BookmarkList
    template_name = "bookmark/public_item_list.html"
    paginate_by = 6

    def get_queryset(self):
        _user = UserProfile.objects.filter(nickname=self.kwargs.get('nickname')).get()
        print(_user)
        if _user:
            _list = get_object_or_404(
                BookmarkList,
                user=_user,
                access_level='S',
                id=self.kwargs.get('pk')
            )
            queryset = _list.bookmarkitem_set.all()
            return queryset
        else:
            # TODO: 임시 방편
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_list_pk'] = self.kwargs.get('pk')
        context['url_nickname'] = self.kwargs.get('nickname')
        return context


def register_favorite_list(request, **kwargs):
    if request.method == "POST":
        user = request.user
        _list = get_object_or_404(BookmarkList, pk=request.POST['list_pk'])

        if _list.user.get() != user:
            _list.fan_of_list.add(user)

            return JsonResponse({
                'cnt': _list.fan_of_list.count()
            })

    return JsonResponse(
        {'status':'false','message': 'register 안돼요'},
        status=500
    )


def delist_favorite_list(request, **kwargs):
    if request.method == "POST":
        user = request.user
        result = user.is_list_fan(request.POST['list_pk'])

        if result and result['is_fan']:
            fan_list = result['list'].fan_of_list
            fan_list.remove(user)

            return JsonResponse({
                'cnt': fan_list.count()
            })

    return JsonResponse(
        {'status':'false','message': 'delist 실패'},
        status=500
    )

def register_favorite_item(request, **kwargs):
    if request.method == "POST":
        user = request.user
        _item = get_object_or_404(BookmarkItem, pk=request.POST['item_pk'])

        if _item.belonged_list.user.get() != user:
            _item.fan_of_item.add(user)

            return JsonResponse({
                'cnt': _item.fan_of_item.count()
            })

    return JsonResponse(
        {'status':'false','message': 'register 안돼요'},
        status=500
    )


def delist_favorite_item(request, **kwargs):
    if request.method == "POST":
        user = request.user
        result = user.is_item_fan(request.POST['item_pk'])

        if result and result['is_fan']:
            fan_list = result['item'].fan_of_item
            fan_list.remove(user)

            return JsonResponse({
                'cnt': fan_list.count()
            })

    return JsonResponse(
        {'status':'false','message': 'delist 실패'},
        status=500
    )
