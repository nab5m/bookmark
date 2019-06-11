from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from bookmark.forms import BookmarkAddForm
from bookmark.models import Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    template_name = 'bookmark/bookmark_add.html'
    form_class = BookmarkAddForm
    success_url = reverse_lazy('bookmark:index')
