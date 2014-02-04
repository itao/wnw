from django.conf.urls import patterns, url

urlpatterns = patterns('supers.views',
    # Console page
    url(r'^$', 'index', name='supers_index'),
    url(r'^students/$', 'students_stats', name='super_students'),
    url(r'^parents/$', 'parents_stats', name='super_parents'),
    url(r'^teachers/$', 'teachers_stats', name='super_teachers'),
)
