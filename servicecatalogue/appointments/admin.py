from django.contrib import admin

from servicecatalogue.appointments.models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass

