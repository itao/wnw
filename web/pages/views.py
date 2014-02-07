from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from klasses.models import Klass

def welcome(request):
    template = 'pages/landing/welcome.html'

    return render(
        request,
        template,
        {
        }
    )

def index(request):
    template = 'pages/app/home.html'

    return render(
        request,
        template,
        {}
    )
