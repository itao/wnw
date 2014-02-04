import json

from django.http import HttpResponse
from django.template import RequestContext, loader

from students.models import Student

def index(request):
    students = Student.objects.all()

    t = loader.get_template('pages/app/students/index.html')
    c = RequestContext(
        request,
        {
            'students': students
        }
    )
    body = t.render(c)

    return HttpResponse(
        json.dumps({
            'title': 'Class Name - Students',
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
