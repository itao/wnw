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

	t = loader.get_template('pages/app/supers/index.html')
	h = loader.get_template('pages/app/supers/index_header.html')
	c = RequestContext(
	    request,
	    {}
	)
	header = h.render(c)
	body = t.render(c)

	return HttpResponse(
        json.dumps({
            'title': 'Super',
            'header': header,
            'body': body,
        }),
        mimetype="application/json"
    )

def students(request):
	template = 'pages/app/supers/students.html'
	students = Student.objects.all()
	names = students.name

	t = loader.get_template(template)
	c = RequestContext(
	    request,
	    {
	        'student': student
	    }
	)
	html = t.render(c)

	return HttpResponse(
	    json.dumps({
	        'title': 'Students Statistics',
	        'html': html,
	    }),
	    mimetype="application/json"
	)

def parents(request):
	template = 'pages/app/supers/parents.html'
	parents = Parent.objects.all()

	t = loader.get_template(template)
	c = RequestContext(
	    request,
	    {
	        'parent': parent
	    }
	)
	html = t.render(c)

	return HttpResponse(
	    json.dumps({
	        'title': 'Parents Statistics',
	        'html': html,
	    }),
	    mimetype="application/json"
	)

def teachers(request):
	template = 'pages/app/supers/teachers.html'
	teachers = Teacher.objects.all()

	t = loader.get_template(template)
	c = RequestContext(
	    request,
	    {
	        'teacher': teacher
	    }
	)
	html = t.render(c)

	return HttpResponse(
	    json.dumps({
	        'title': 'Teachers Statistics',
	        'html': html,
	    }),
	    mimetype="application/json"
	)