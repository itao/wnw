from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',
    url(r'^$', 'index', name='accounts_index'),
    url(r'^login$', 'login', name='accounts_login'),
    url(r'^signup$', 'signup', name='accounts_signup'),
)
