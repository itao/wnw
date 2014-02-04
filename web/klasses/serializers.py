from rest_framework import serializers as s

from .models import Klass

class KlassSerializer(s.ModelSerializer):
    colour = s.CharField(required=False)
    code = s.CharField(required=False)

    class Meta:
        model = Klass
        fields = ('teacher', 'title', 'code', 'start', 'end', 'colour')

