from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

from accounts.models import UserProfile


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=36, label='아이디', widget=forms.TextInput(
        attrs={'class': 'form-control mt-2'}
    ))
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control mt-2'}
    ))

    error_messages = {
        'invalid_login': _(
            "아이디나 비밀번호를 확인해주세요"
        ),
        'inactive': _("이 계정은 사용정지 되었습니다"),
    }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)
        # TODO: 이거 왜 그런거지?

    class Meta:
        model = UserProfile
        fields = ['username', 'password']
        # TODO: add validator
