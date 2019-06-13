from django.urls import path, reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView

from bookmark.models import Bookmark
from bookmark.views import BookmarkCreateView, BookmarkUpdateView

app_name="bookmark"

urlpatterns = [
    path('', ListView.as_view(model=Bookmark, paginate_by=5), name="index"),
    path('add/', BookmarkCreateView.as_view(), name="add"),
    path('delete/<int:pk>/', DeleteView.as_view(
            model=Bookmark,
            success_url=reverse_lazy('bookmark:index'),
        ), name="delete",
    ),
    path('detail/<int:pk>', DetailView.as_view(model=Bookmark), name="detail"),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name="update"),
]
