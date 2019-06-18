from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

from accounts.models import UserProfile
from bookmark.forms import ListForm, ItemForm
from bookmark.models import BookmarkItem, BookmarkList


class BookmarkListView(ListView):
    model = BookmarkList
    template_name = "bookmark/bookmark_list.html"
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = get_list_or_404(BookmarkList, user=self.request.user)
            return queryset
        else:
            # TODO: 임시 방편
            return []


class ListUpdateView(UpdateView):
    model = BookmarkList
    template_name = 'bookmark/list_update.html'
    form_class = ListForm
    success_url = reverse_lazy('bookmark:index')


class ListCreateView(CreateView):
    model = BookmarkList
    template_name = 'bookmark/list_add.html'
    form_class = ListForm
    success_url = reverse_lazy('bookmark:index')


class ItemListView(ListView):
    model = BookmarkItem
    template_name = "bookmark/item_list.html"
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = get_list_or_404(BookmarkItem, belonged_list=self.kwargs['pk'])
            return queryset
        else:
            # TODO: 임시 방편
            return []


class ItemCreateView(CreateView):
    model = BookmarkItem
    template_name = 'bookmark/item_add.html'
    form_class = ItemForm

    def get_success_url(self):
        return reverse_lazy(
            'bookmark:item_list',
            args=[self.request.resolver_match.kwargs['pk']],
        )

    def form_valid(self, form):
        list_pk = self.request.resolver_match.kwargs['pk']
        form.instance.belonged_list = BookmarkList.objects.get(pk=list_pk)
        return super(ItemCreateView, self).form_valid(form)


class ItemDeleteView(DeleteView):
    model = BookmarkItem
    template_name = 'bookmark/item_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy(
            'bookmark:item_list',
            args=[self.request.resolver_match.kwargs['list_pk']],
        )


class ItemDetailView(DetailView):
    model = BookmarkItem
    template_name = 'bookmark/item_detail.html'


class ItemUpdateView(UpdateView):
    model = BookmarkItem
    template_name = 'bookmark/item_update.html'
    form_class = ItemForm

    def get_success_url(self):
        return reverse_lazy(
            'bookmark:item_list',
            args=[self.request.resolver_match.kwargs['pk']],
        )


class PublicBookmarkListView(ListView):
    model = BookmarkList
    template_name = "bookmark/public_bookmark_list.html"
    paginate_by = 5

    def get_queryset(self):
        _user = UserProfile.objects.filter(username=self.request.resolver_match.kwargs['nickname']).get()
        print(_user)
        if _user:
            queryset = get_list_or_404(BookmarkList, user=_user, access_level='S')
            return queryset
        else:
            # TODO: 임시 방편
            return []


class PublicItemListView(ListView):
    model = BookmarkList
    template_name = "bookmark/public_item_list.html"
    paginate_by = 5

    def get_queryset(self):
        _user = UserProfile.objects.filter(username=self.request.resolver_match.kwargs['nickname']).get()
        print(_user)
        if _user:
            _list = get_object_or_404(
                BookmarkList,
                user=_user,
                access_level='S',
                id=self.request.resolver_match.kwargs['pk']
            )
            queryset = _list.bookmarkitem_set.all()
            return queryset
        else:
            # TODO: 임시 방편
            return []
