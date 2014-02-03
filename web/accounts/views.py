from django.shortcuts import render

from rest_framework import viewsets

from .models import User

class UserViewSet(viewsets.ModelViewSet):
    model = User

def index(request):
    template = 'pages/console/accounts/index.html'

    return render(
        request,
        template,
        {}
    )


def signup(request):
    template = 'pages/console/accounts/signup.html'

    return render(
        request,
        template,
        {}
    )


def login(request):
    template = 'pages/console/accounts/login.html'

    return render(
        request,
        template,
        {}
    )
