from django import VERSION

from example.app.views import app_index

if VERSION <= (2, 2):
    from django.conf.urls import url
else:
    from django.urls import re_path as url

urlpatterns = [
    url(r"^$", app_index, name="app_index"),
]
