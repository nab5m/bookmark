from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class UsernameValidator(ASCIIUsernameValidator):
    regex = r'^[\w-_]+\Z'
    message = _(
        '영문자, 숫자, - 또는 _만 사용 가능합니다.'
    )


class UserProfile(AbstractUser):
    username_validator = UsernameValidator()
    username = models.CharField(
        _('아이디'),
        max_length=36,
        unique=True,
        help_text= _('필수 항목. 36자 이하로 영문자, 숫자, - 또는 _만 사용 가능합니다.'),
        validators=[username_validator],
        error_messages={
            'unique': _("해당 아이디는 이미 존재합니다."),
        }
    )
    email = models.EmailField(_('이메일'), blank=True)

    name = models.CharField(_('이름'), max_length=15, blank=True)
    first_name = last_name = None


    REQUIRED_FIELDS = []
    # username과 password는 required, AbstractUser에서는 email도
