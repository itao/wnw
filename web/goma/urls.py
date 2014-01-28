from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^', include('pages.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
