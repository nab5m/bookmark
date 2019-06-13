from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from accounts.forms import LoginForm, PWChangeForm, RegistrationForm, PWResetForm, PWResetEmailForm


# def index(request): # temporary
#    return HttpResponse('Hello')


def logout_success(request):
    if not request.user.is_authenticated:
        return render(request, 'accounts/logout_success.html')
    # TODO: redirect


def register_success(request):
    if not request.user.is_authenticated:
        return render(request, 'accounts/register_success.html')
    # TODO: redirect


class RegistrationView(FormView):
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('accounts:register_success')
    form_class = RegistrationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomPWChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:password_change_done')
    form_class = PWChangeForm


class PWResetEmailView(PasswordResetView):
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    template_name = 'accounts/password_reset_form.html',
    form_class = PWResetEmailForm,
