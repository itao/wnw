from rest_framework import serializers as s

from .models import Experience

class ExperienceSerializer(s.ModelSerializer):

    class Meta:
        model = Experience
        fields = ('id','name', 'description', 'location', 'start', 'end', 'attending')

