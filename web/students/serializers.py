from rest_framework import serializers as s

from .models import Student
from klasses.serializers import KlassSerializer

class StudentSerializer(s.ModelSerializer):
    klasses = KlassSerializer(many=True)
    class Meta:
        model = Student
        fields = ('account', 'picture', 'klasses')

