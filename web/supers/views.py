# Create your views here.
import json

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader

from students.models import Student
from parents.models import Parent
from teachers.models import Teacher

def index(request):
	'pages/app/supers/index.html'

	b = loader.get_template('pages/app/supers/index.html')
	h = loader.get_template('pages/app/supers/index_header.html')
	c = RequestContext(
	    request,
	    {
	    	'students': Student.objects.all()
	    }
	)
	header = h.render(c)
	body = b.render(c)

	return HttpResponse(
        json.dumps({
            'title': 'Super',
            'header': header,
            'body': body,
        }),
        mimetype="application/json"
    )


# def get_parents(request):
# 	parents = Parent.objects.all()
# 	pass

# def get_teachers(request):
# 	teachers = Teacher.objects.all()
# 	pass