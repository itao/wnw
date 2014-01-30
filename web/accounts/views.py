from django.shortcuts import render


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
