from django.conf.urls import patterns, url

urlpatterns = patterns('students.views',
    # Console page
    url(r'^$', 'index', name='students_index'),
    url(r'^(?P<student_id>\d+)$', 'profile', name='students_profile'),
)
