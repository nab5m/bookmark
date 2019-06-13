from django.urls import path, reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView

from bookmark.models import BookmarkItem, BookmarkList
from bookmark.views import ListCreateView, BookmarkListView, \
    ListUpdateView, ItemListView, ItemCreateView, ItemDeleteView, ItemDetailView, ItemUpdateView

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

    path('<int:pk>/', ItemListView.as_view(), name="item_list"),
    path('<int:pk>/add/', ItemCreateView.as_view(), name="add_item"),
    path('<int:list_pk>/delete/<int:pk>/', ItemDeleteView.as_view(), name="delete_item"),
    path('<int:list_pk>/detail/<int:pk>', ItemDetailView.as_view(), name="item_detail"),
    path('<int:list_pk>/update/<int:pk>', ItemUpdateView.as_view(), name="update_item"),
]
