from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from bookmark.forms import BookmarkForm
from bookmark.models import BookmarkItem


class BookmarkCreateView(CreateView):
    model = BookmarkItem
    template_name = 'bookmark/bookmark_add.html'
    form_class = BookmarkForm
    success_url = reverse_lazy('bookmark:index')

class BookmarkUpdateView(UpdateView):
    model = BookmarkItem
    template_name = 'bookmark/bookmark_update.html'
    form_class = BookmarkForm
