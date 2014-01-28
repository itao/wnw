from django.conf.urls import patterns, url

urlpatterns = patterns('students.views',
    # Console page
    url(r'^$', 'index', name='students_index'),
    url(r'^portfolio$', 'portfolio', name='students_portfolio'),
)
