from django.urls import path, reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView

from bookmark.models import BookmarkItem, BookmarkList
from bookmark.views import BookmarkItemCreateView, BookmarkItemUpdateView

app_name="bookmark"

urlpatterns = [
    path('', ListView.as_view(
            model=BookmarkList,
            template_name="bookmark/bookmark_list.html",
            paginate_by=5,
        ), name="index"
     ),
    # path('', ListView.as_view(model=BookmarkItem, paginate_by=5), name="index"),
    # path('add/', BookmarkItemCreateView.as_view(), name="add"),
    # path('delete/<int:pk>/', DeleteView.as_view(
    #        model=BookmarkItem,
    #        success_url=reverse_lazy('bookmark:index'),
    #    ), name="delete",
    # ),
    # path('detail/<int:pk>', DetailView.as_view(model=BookmarkItem), name="detail"),
    # path('update/<int:pk>', BookmarkItemUpdateView.as_view(), name="update"),
]
