from django.shortcuts import render

def index(request):
    template = 'pages/console/accounts/index.html'

    return render(
        request,
        template,
        {}
    )
