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
    REQUIRED_FIELDS = ['first_name', 'last_name']

    email = m.EmailField(max_length=255, unique=True)
    is_active = m.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
            'active. Unselect this instead of deleting accounts.'))
    first_name = m.CharField(max_length=1024)
    last_name = m.CharField(max_length=1024)

    objects = UserManager()

    def get_full_name(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __unicode__(self):
        return u'<User: {}>'.format(self.email)

    @property
    def is_staff(self):
        return self.is_superuser and self.is_active

