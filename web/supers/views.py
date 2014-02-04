# Create your views here.
import json

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader

from students.models import Student
from parents.models import Parent
from teachers.models import Teacher

def index(request):

	b = loader.get_template('pages/app/supers/index.html')
	h = loader.get_template('pages/app/supers/index_header.html')
	n = loader.get_template('pages/app/supers/index_nav.html')
	c = RequestContext(
	    request,
	    {
	    	'students': Student.objects.all(),
	    	'parents': Parent.objects.all(),
	    	'teachers': Teacher.objects.all(),
	    }
	)
	header = h.render(c)
	body = b.render(c)
	nav = n.render(c)

	return HttpResponse(
        json.dumps({
            'title': 'Super',
            'header': header,
            'body': body,
            'nav': nav,
        }),
        mimetype="application/json"
    )


# def get_parents(request):
# 	parents = Parent.objects.all()
# 	pass

# def get_teachers(request):
# 	teachers = Teacher.objects.all()
# 	pass