## Script to create sample data
from datetime import datetime

from accounts.models import User
from teachers.models import Teacher
from students.models import Student
from klasses.models import Klass
from notes.models import Note


def clean():
    User.objects.all().delete()
    Teacher.objects.all().delete()
    Student.objects.all().delete()
    Klass.objects.all().delete()
    Note.objects.all().delete()


def init():
    # Wipe db
    clean()

    # Create users
    u = User(first_name='Demo', last_name='Teacher', email='demo@sesame.io')
    u.save()
    u.set_password('sesame')
    u.save()

    # Create teachers
    t = Teacher(account=u)
    t.save()

    # Create classes
    for i in range(3):
        index = str(i+1)
        name = 'Class #' + index
        code = 'KLS' + index
        start = end = datetime.now().date()
        colour = "#" + index*6

        k = Klass(teacher=t, name=name, code=code, start=start, end=end, colour=colour)
        k.save()

    # Create students
    students = [
        {
            'first_name': 'Alton',
            'last_name': 'Lau',
            'email': 'alton@lau.com'
        }, {
            'first_name': 'Marc',
            'last_name': 'Lo',
            'email': 'marc@lo.com'
        }, {
            'first_name': 'Madigan',
            'last_name': 'Kim',
            'email': 'madigan@kim.com'
        }
    ]
    classes = Klass.objects.all()
    for i in range(3):
        s = students[i]
        u = User(first_name=s['first_name'], last_name=s['last_name'], email=s['email'])
        u.save()
        s = Student(account=u)
        s.save()
        s.klasses = classes[:i+1]


    k = Klass.objects.all()[0]
    s = Student.objects.all()
    # Create notes
    for i in range(3):
        index = str(i+1)
        detail = 'This is note #' + index
        n = Note(klass=k, detail=detail)
        n.save()
        n.students = s[:i+1]