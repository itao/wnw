from rest_framework import viewsets

from .models import User

class UserViewSet(viewsets.ModelViewSet):
    model = User
