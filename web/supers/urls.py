from django.conf.urls import patterns, url

urlpatterns = patterns('supers.views',
    # Console page
    url(r'^$', 'index', name='supers_index'),
)
