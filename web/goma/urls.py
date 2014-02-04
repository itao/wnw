from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static

from .routers import router

urlpatterns = patterns('',
    url(r'^', include('pages.urls')),

    # HACK to allow api without trailing /
    url(r'^api$', include(router.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
