from django import VERSION
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve


admin.autodiscover()

urlpatterns = [
    url(r'^', include('example.app.urls')),
    url(r'^admin/', include(admin.site.urls) if VERSION < (2, 0) else admin.site.urls),
]

urlpatterns += [
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], serve,
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
]
