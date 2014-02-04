from django.shortcuts import render

def index(request):
    template = 'pages/console/students/index.html'

    return render(
        request,
        template,
        {
        }
    )

def profile(request):
    template = 'pages/app/students/profile.html'

    return render(
        request,
        template,
        {
        }
    )

