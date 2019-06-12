from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views

import accounts.views
from accounts.forms import PWResetForm, CustomSetPWForm

app_name = 'accounts'

urlpatterns = [
    path('', accounts.views.index, name="index"),
    path('login/', accounts.views.CustomLoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('accounts:logout_success')), name="logout"),
    path('logout-success/', accounts.views.logout_success, name="logout_success"),
    path('register/', accounts.views.RegistrationView.as_view(), name="register"),
    path('register-success/', accounts.views.register_success, name="register_success"),

    path('password-change/', accounts.views.CustomPWChangeView.as_view(), name="password_change"),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name="accounts/password_change_success.html"), name="password_change_done"),

    path('password-reset/', accounts.views.CustomPWResetView.as_view(
            template_name='accounts/password_reset_form.html',
            form_class=PWResetForm
        ), name='password_reset'
    ),
    path('password-reset/done/', PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
        ), name="password_reset_done"
    ),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('accounts:password_reset_complete'),
            template_name='accounts/password_reset_confirm.html',
            form_class=CustomSetPWForm
        ), name="password_reset_confirm"
    ),
    path('reset/done/', PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
        ), name="password_reset_complete"
    ),
]
