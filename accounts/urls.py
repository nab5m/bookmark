from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

import accounts.views as accounts_views
from accounts.forms import LoginForm, PWResetForm

app_name = 'accounts'

urlpatterns = [
    # path('', accounts_views.index, name="index"),
    path('login/', auth_views.LoginView.as_view(
            template_name = 'accounts/login.html',
            form_class = LoginForm,
        ), name="login"
    ),
    path('logout/', auth_views.LogoutView.as_view(
            next_page=reverse_lazy('accounts:logout_success'),
        ), name="logout"
    ),
    path('logout-success/', accounts_views.logout_success, name="logout_success"),
    path('register/', accounts_views.RegistrationView.as_view(), name="register"),
    path('register-success/', accounts_views.register_success, name="register_success"),

    path('password-change/', accounts_views.CustomPWChangeView.as_view(), name="password_change"),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
            template_name="accounts/password_change_success.html"
        ), name="password_change_done"
    ),

    path('password-reset/', accounts_views.PWResetEmailView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html',
        ), name="password_reset_done"
    ),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('accounts:password_reset_complete'),
            template_name='accounts/password_reset_confirm.html',
            form_class=PWResetForm,
        ), name="password_reset_confirm"
    ),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
        ), name="password_reset_complete"
    ),
]
