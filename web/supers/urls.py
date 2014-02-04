from django.conf.urls import patterns, url

urlpatterns = patterns('supers.views',
    # Console page
    url(r'^$', 'index', name='supers_index'),
    url(r'^students/$', 'students', name='super_students'),
    url(r'^parents/$', 'parents', name='super_parents'),
    url(r'^teachers/$', 'teachers', name='super_teachers'),
)
