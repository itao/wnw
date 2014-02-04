# Create your views here.
import json

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader

from students.models import Student
from parents.models import Parent
from teachers.models import Teacher

def index(request):
	template = 'layouts/app_base.html'
    
	return HttpResponse(
        json.dumps({
            'title': 'Class Name - Students',
            'html': html,
        }),
        mimetype="application/json"
    )

def students_stats(request):
	template = 'layouts/app_base.html'
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
	        'title': student.name(),
	        'html': html,
	    }),
	    mimetype="application/json"
	)

def parents_stats(request):
	template = 'layouts/app_base.html'
	parents = Parent.objects.all()

	return HttpResponse(
	    json.dumps({
	        'title': student.name(),
	        'html': html,
	    }),
	    mimetype="application/json"
	)

def teachers_stats(request):
	template = 'layouts/app_base.html'
	teachers = Teacher.objects.all()

	return HttpResponse(
	    json.dumps({
	        'title': student.name(),
	        'html': html,
	    }),
	    mimetype="application/json"
	)