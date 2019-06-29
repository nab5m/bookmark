from django.urls import path

from app_index.views import IndexTemplateView, login_test_user

urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index"),
    path('index/', IndexTemplateView.as_view()),
    path('login-test-user/<int:num>/', login_test_user, name="login_test_user"),
]
