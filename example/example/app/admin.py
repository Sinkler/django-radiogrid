from django.contrib import admin

from example.app.models import Octodex, OptionalGridModel


class OctodexAdmin(admin.ModelAdmin):
    pass


admin.site.register(Octodex, OctodexAdmin)
admin.site.register(OptionalGridModel)
