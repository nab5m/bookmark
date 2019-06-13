from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

from bookmark.forms import ListForm, ItemForm
from bookmark.models import BookmarkItem, BookmarkList


class BookmarkListView(ListView):
    model = BookmarkList
    template_name = "bookmark/bookmark_list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = super(BookmarkListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class ListUpdateView(UpdateView):
    model = BookmarkList
    template_name = 'bookmark/list_update.html'
    form_class = ListForm


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
        queryset = super(ItemListView, self).get_queryset()
        queryset = queryset.filter(belonged_list=self.kwargs['pk'])
        return queryset


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