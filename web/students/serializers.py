from rest_framework import serializers as s

from .models import Student
from klasses.serializers import KlassSerializer

class StudentSerializer(s.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id','account', 'picture', 'klasses')
