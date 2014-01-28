from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('pages.views',
    url(r'^$', 'home', name='home'),
    url(r'^welcome$', TemplateView.as_view(template_name='pages/welcome.html'), name='welcome'),
)
