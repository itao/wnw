from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required

@login_required
def app(request):
    if request.user.type == 'teacher':
        template = 'teach.html'
    elif request.user.type == 'student':
        template = 'learn.html'
    elif request.user.type == 'parent':
        tempalte = 'observe.html'
    else:
        raise Http404

    return render(request, template, {} )
