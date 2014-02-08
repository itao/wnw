from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',
    url(r'^$', 'index', name='accounts_index'),
    url(r'^portal$', 'portal', name='accounts_portal'),
    url(r'^oauth2login$', 'oauth2login', name='accounts_oauth2_login'),
    url(r'^google/login/callback/$', 'oauth2callback', name='accounts_oauth2_callback'),
)
