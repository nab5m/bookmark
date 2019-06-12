from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from accounts.forms import LoginForm, AccountCreationForm, PWChangeForm


def index(request): # temporary
    return HttpResponse('Hello')


def logout_success(request):
    if not request.user.is_authenticated:
        return render(request, 'accounts/logout_success.html')


def register_success(request):
    if not request.user.is_authenticated:
        return render(request, 'accounts/register_success.html')


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm


class RegistrationView(FormView):
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('accounts:register_success')
    form_class = AccountCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomPWChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:password_change_done')
    form_class = PWChangeForm


class CustomPWResetView(PasswordResetView):
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
