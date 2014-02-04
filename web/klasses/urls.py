from django.conf.urls import patterns, url

urlpatterns = patterns('klasses.views',
    # Console page
    url(r'^add$', 'add', name='classes_add'),
)
