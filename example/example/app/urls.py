from django.conf.urls import patterns, url

urlpatterns = patterns(
    'example.app.views',
    url(r'^$', 'app_index', name='app_index'),
)
