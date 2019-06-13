from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm, \
    SetPasswordForm
from django.utils.translation import gettext_lazy as _

from accounts.models import UserProfile


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=36,
        label=_('아이디'),
        widget=forms.TextInput(
            attrs={'class': 'form-control mt-2'},
        ),
    )
    password = forms.CharField(
        label=_('비밀번호'),
        widget=forms.PasswordInput(
            attrs={'class': 'form-control mt-2'},
        )
    )

    error_messages = {
        'invalid_login': _(
            "아이디나 비밀번호를 확인해주세요"
        ),
        'inactive': _("이 계정은 사용정지 되었습니다"),
    }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)
        # TODO: 이거 왜 그런거지? - AuthForm이 이미 request를 가지고 있다고 본거 같기도

    class Meta:
        model = UserProfile
        fields = ['username', 'password']
        # TODO: add validator


class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mt-2'

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2', 'name')


class PWChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mt-2'


class PWResetEmailForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mt-2'
            if field_name == 'email':   # TODO: why not use gettext function
                field.label = '이메일'
                field.help_text = \
                    '아래의 이메일로 안내 메시지가 전송됩니다. '\
                    '회원가입 시 입력한 이메일을 입력해주세요.'


class PWResetForm(SetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mt-2'
