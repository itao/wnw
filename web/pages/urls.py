from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('pages.views',
    # Landing pages
    url(r'^welcome$', TemplateView.as_view(template_name='pages/landing/welcome.html'), name='welcome'),

    # Console pages
    url(r'^$', TemplateView.as_view(template_name='pages/console/home.html'), name='home'),
)
