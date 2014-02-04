from django.shortcuts import render

from rest_framework import viewsets

from .models import User

class UserViewSet(viewsets.ModelViewSet):
    model = User

def index(request):
    template = 'pages/app/accounts/index.html'

    return render(
        request,
        template,
        {}
    )


def portal(request):
    template = 'layouts/login_base.html'

    return render(
        request,
        template,
        {}
    )
