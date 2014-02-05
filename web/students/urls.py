from django.conf.urls import patterns, url

urlpatterns = patterns('students.views',
    # Console page
    url(r'^$', 'index', name='students_index'),
    url(r'^enroll$', 'enroll', name='students_enroll'),
    url(r'^(?P<student_id>\d+)$', 'profile', name='students_profile'),
    url(r'^(?P<student_id>\d+)/about$', 'about', name='students_about'),
    url(r'^(?P<student_id>\d+)/posts$', 'posts', name='students_posts'),
    url(r'^(?P<student_id>\d+)/report$', 'report', name='students_report'),
)
