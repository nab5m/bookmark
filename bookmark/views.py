from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from bookmark.forms import BookmarkForm, ListForm
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
    template_name = "bookmark/bookmark_item_list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = super(ItemListView, self).get_queryset()
        queryset = queryset.filter(belonged_list=self.kwargs['pk'])
        return queryset


class BookmarkItemCreateView(CreateView):
    model = BookmarkItem
    template_name = 'bookmark/bookmark_add.html'
    form_class = BookmarkForm
    success_url = reverse_lazy('bookmark:index')


class BookmarkItemUpdateView(UpdateView):
    model = BookmarkItem
    template_name = 'bookmark/bookmark_update.html'
    form_class = BookmarkForm
