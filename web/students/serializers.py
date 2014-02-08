from rest_framework import serializers as s

from .models import Student
from accounts.serializers import UserSerializer

class StudentSerializer(s.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id','first_name', 'last_name', 'email', 'picture', 'klasses')
