from django import VERSION
from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.views.static import serve

if VERSION <= (2, 2):
    from django.conf.urls import url
else:
    from django.urls import re_path as url


admin.autodiscover()

urlpatterns = [
    url(r"^", include("example.app.urls")),
    url(r"^admin/", include(admin.site.urls) if VERSION < (2, 0) else admin.site.urls),
]

urlpatterns += [
    url(
        r"^%s(?P<path>.*)$" % settings.MEDIA_URL[1:],
        serve,
        {"document_root": settings.MEDIA_ROOT, "show_indexes": True},
    ),
]
