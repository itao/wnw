from django.db import models as m

from goma.model_mixins import TimestampedMixin
from accounts.models import User

class Experience(TimestampedMixin):
    name = m.TextField()
    description = m.TextField(null=True, blank=True)
    picture = m.ImageField(null=True, blank=True, upload_to='experiences/pictures')
    start = m.DateTimeField()
    end = m.DateTimeField()
    location = m.TextField(null=True, blank=True)

    attending = m.ManyToManyField(User, related_name='experiences')

    def __unicode__(self):
        return u'<Experience: {}>'.format(self.name)
