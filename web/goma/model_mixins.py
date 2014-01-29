from django.db import models as m
from django.utils import timezone

class TimestampedMixin(m.Model):
    created = m.DateTimeField(editable=False, default=timezone.now)
    updated = m.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
