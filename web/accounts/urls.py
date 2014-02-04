from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',
    url(r'^$', 'index', name='accounts_index'),
    url(r'^portal$', 'portal', name='accounts_portal'),
)
