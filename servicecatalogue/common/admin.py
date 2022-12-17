from django.contrib import admin

from servicecatalogue.common.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass
