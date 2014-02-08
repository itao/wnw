from rest_framework import serializers as s

from .models import User

class UserSerializer(s.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'email')

