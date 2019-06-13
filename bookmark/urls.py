from django.urls import path, reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView

from bookmark.models import BookmarkItem, BookmarkList
from bookmark.views import BookmarkItemCreateView, BookmarkItemUpdateView, ListCreateView, BookmarkListView, \
    ListUpdateView

app_name="bookmark"

urlpatterns = [
    path('', BookmarkListView.as_view(), name="index"),
    path('add/', ListCreateView.as_view(), name="add_list"),
    path('delete/<int:pk>', DeleteView.as_view(
            model=BookmarkList,
            success_url=reverse_lazy('bookmark:index'),
            template_name='bookmark/list_confirm_delete.html',
        ), name="delete_list"
    ),
    path('update/<int:pk>', ListUpdateView.as_view(), name="update_list"),
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
