from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('pages.views',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^app$', 'app', name='app'),
    url(r'^login$', TemplateView.as_view(template_name='login.html'), name='login'),
)
