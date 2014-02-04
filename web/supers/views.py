# Create your views here.
import json

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader

from students.models import Student
from parents.models import Parent
from teachers.models import Teacher

def index(request):
	template = 'pages/app/supers/index.html'
    
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
            'title': 'Class Name - Students',
            'html': html,
        }),
        mimetype="application/json"
    )

def students_stats(request):
	template = 'pages/app/supers/students_stats.html'
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

def parents_stats(request):
	template = 'pages/app/supers/parents_stats.html'
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

def teachers_stats(request):
	template = 'pages/app/supers/teachers_stats.html'
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