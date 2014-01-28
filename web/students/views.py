from django.shortcuts import render

def index(request):
    template = 'pages/console/students/index.html'

    return render(
        request,
        template,
        {
        }
    )

def portfolio(request):
    template = 'pages/console/students/portfolio.html'

    return render(
        request,
        template,
        {
        }
    )

