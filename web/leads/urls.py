from django.conf.urls import patterns, url

urlpatterns = patterns('leads.views',
    # Console page
    url(r'^$', 'index', name='leads_index'),
)
