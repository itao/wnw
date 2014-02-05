import json

from django.http import HttpResponse
from django.template import RequestContext, loader

from students.models import Student
from klasses.models import Klass

def index(request):
    students = Student.objects.all()

    t = loader.get_template('pages/app/students/index.html')
    h = loader.get_template('pages/app/students/index_header.html')
    c = RequestContext(
        request,
        {
            'students': students
        }
    )
    header = h.render(c)
    body = t.render(c)

    return HttpResponse(
        json.dumps({
            'title': 'Class name',
            'header': header,
            'body': body,
        }),
        mimetype="application/json"
    )


def enroll(request):
    classes = Klass.objects.all()

    t = loader.get_template('pages/app/students/enroll.html')
    h = loader.get_template('pages/app/students/enroll_header.html')
    c = RequestContext(
        request,
        {}
    )
    header = h.render(c)
    body = t.render(c)

    return HttpResponse(
        json.dumps({
            'title': 'Class name',
            'header': header,
            'body': body,
        }),
        mimetype="application/json"
    )



def profile(request, student_id):
    student = Student.objects.get(pk=student_id)

    t = loader.get_template('pages/app/students/profile.html')
    h = loader.get_template('pages/app/students/profile_header.html')
    c = RequestContext(
        request,
        {
            'student': student
        }
    )
    header = h.render(c)
    body = t.render(c)

    return HttpResponse(
        json.dumps({
            'header': header,
            'body': body,
        }),
        mimetype="application/json"
    )


def about(request, student_id):
    student = Student.objects.get(pk=student_id)

    t = loader.get_template('pages/app/students/about.html')
    c = RequestContext(
        request,
        {}
    )
    html = t.render(c)

    return HttpResponse(
        json.dumps({
            'html': html,
        }),
        mimetype="application/json"
    )


def posts(request, student_id):
    student = Student.objects.get(pk=student_id)

    t = loader.get_template('pages/app/students/posts.html')
    c = RequestContext(
        request,
        {}
    )
    html = t.render(c)

    return HttpResponse(
        json.dumps({
            'html': html,
        }),
        mimetype="application/json"
    )

def report(request, student_id):
    student = Student.objects.get(pk=student_id)

    t = loader.get_template('pages/app/students/report.html')
    c = RequestContext(
        request,
        {}
    )
    html = t.render(c)

    return HttpResponse(
        json.dumps({
            'html': html,
        }),
        mimetype="application/json"
    )
