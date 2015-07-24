from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin


admin.autodiscover()

js_info_dict = {
    'packages': ('django.conf',),
}

urlpatterns = patterns(
    '',
    url(r'^', include('example.app.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(
    '',
    (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
