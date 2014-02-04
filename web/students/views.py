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
            'title': 'Students',
            'header': header,
            'body': body,
        }),
        mimetype="application/json"
    )


def add(request):
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
            'title': 'Enroll Students',
            'header': header,
            'body': body,
        }),
        mimetype="application/json"
    )



def profile(request, student_id):
    student = Student.objects.get(pk=student_id)

    t = loader.get_template('pages/app/students/profile.html')
    c = RequestContext(
        request,
        {
            'student': student
        }
    )
    body = t.render(c)

    return HttpResponse(
        json.dumps({
            'title': student.name(),
            'body': body,
        }),
        mimetype="application/json"
    )
