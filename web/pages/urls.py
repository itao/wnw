from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('pages.views',
    url(r'^$', 'index', name='index'),

    # Landing pages
    url(r'^welcome$', TemplateView.as_view(template_name='pages/landing/welcome.html'), name='welcome'),
)
