import json

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader

from students.models import Student

def index(request):
    template = 'pages/app/students/index.html'

    students = Student.objects.all()

    t = loader.get_template(template)
    c = RequestContext(
        request,
        {
            'students': students
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


def profile(request, student_id):
    student = Student.objects.get(pk=student_id)

    template = 'pages/app/students/profile.html'

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
