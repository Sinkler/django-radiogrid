from django.conf.urls import url
from example.app.views import app_index

urlpatterns = [
    url(r'^$', app_index, name='app_index'),
]
