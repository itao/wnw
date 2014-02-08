from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from klasses.models import Klass

def welcome(request):
    template = 'pages/landing/welcome.html'

    return render(
        request,
        template,
        {
        }
    )

@login_required
def index(request):
    if request.user.type == 'teacher':
        template = 'teach.html'
    elif request.user.type == 'student':
        template = 'learn.html'
    elif request.user.type == 'parent':
        tempalte = 'observe.html'
    else:
        raise Http404

    return render(request, template, {} )
