from django.contrib.auth import models as authm
from django.db import models as m
from django.utils.translation import ugettext_lazy as _

from goma.model_mixins import TimestampedMixin

class UserManager(authm.BaseUserManager):

    def create_user(self, email, password=None):
        u = self.model(
            email=self.normalize_email(email),
            password=password,
            is_superuser=False,
            is_staff=False)
        u.save()
        return u

    def create_superuser(self, email, password):
        u = self.model(
            email=self.normalize_email(email),
            password=password,
            is_superuser=True,
            is_staff=True)
        u.save()
        return u

class User(authm.AbstractBaseUser, authm.PermissionsMixin, TimestampedMixin):
    USERNAME_FIELD = 'email'

    email = m.EmailField(max_length=255, unique=True)
    is_staff = m.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
            'site.'))
    is_active = m.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
            'active. Unselect this instead of deleting accounts.'))

    objects = UserManager()
