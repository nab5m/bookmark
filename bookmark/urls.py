from django.urls import path, reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView

from bookmark.models import BookmarkItem, BookmarkList
from bookmark.views import ListCreateView, BookmarkListView, \
    ListUpdateView, ItemListView, ItemCreateView, ItemDeleteView, ItemDetailView, ItemUpdateView
from config.library.views import custom_login_required

app_name = "bookmark"

urlpatterns = [
    path('', BookmarkListView.as_view(), name="index"),
    path('add/', custom_login_required(ListCreateView.as_view()), name="add_list"),
    path('delete/<int:pk>', custom_login_required(DeleteView.as_view(
            model=BookmarkList,
            success_url=reverse_lazy('bookmark:index'),
            template_name='bookmark/list_confirm_delete.html',
        )), name="delete_list"
    ),
    path('update/<int:pk>', custom_login_required(ListUpdateView.as_view()), name="update_list"),

    path('<int:pk>/', ItemListView.as_view(), name="item_list"),
    path('<int:pk>/add/', custom_login_required(ItemCreateView.as_view()), name="add_item"),
    path('<int:list_pk>/delete/<int:pk>/', custom_login_required(ItemDeleteView.as_view()), name="delete_item"),
    path('<int:list_pk>/detail/<int:pk>', custom_login_required(ItemDetailView.as_view()), name="item_detail"),
    path('<int:list_pk>/update/<int:pk>', custom_login_required(ItemUpdateView.as_view()), name="update_item"),
]
