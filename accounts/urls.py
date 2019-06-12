from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views

import accounts.views

app_name = 'accounts'

urlpatterns = [
    path('', accounts.views.index, name="index"),
    path('login/', accounts.views.CustomLoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('accounts:logout_success')), name="logout"),
    path('logout-success/', accounts.views.logout_success, name="logout_success")
]
