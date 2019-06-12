from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from accounts.forms import LoginForm


def index(request): # temporary
    return HttpResponse('Hello')


def logout_success(request):
    if not request.user.is_authenticated:
        return render(request, 'accounts/logout_success.html')


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
