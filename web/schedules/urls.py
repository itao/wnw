from django.conf.urls import patterns, url

urlpatterns = patterns('schedules.views',
    # Console page
    url(r'^$', 'index', name='schedules_index'),
)
