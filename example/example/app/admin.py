from django.contrib import admin

from example.app.models import Octodex


class OctodexAdmin(admin.ModelAdmin):
    pass

admin.site.register(Octodex, OctodexAdmin)
