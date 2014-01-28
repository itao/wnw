from django.shortcuts import render

def index(request):
    template = 'pages/console/schedules/index.html'

    return render(
        request,
        template,
        {
        }
    )
