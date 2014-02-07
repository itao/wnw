from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('pages.views',
    url(r'^$', 'index', name='index'),

    # Landing pages
    url(r'^welcome$', TemplateView.as_view(template_name='pages/landing/welcome.html'), name='welcome'),

    # Console pages
    url(r'^accounts/', include('accounts.urls')),
    url(r'^teachers/', include('teachers.urls')),
    url(r'^classes/', include('klasses.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^schedules/', include('schedules.urls')),
)
