from django.db import models

from servicecatalogue.accounts.models import ProviderProfile, CustomerProfile
from servicecatalogue.common.models import Service
from datetime import datetime


class Appointment(models.Model):
    class Meta:
        unique_together = ('provider', 'date', 'timeslot')

    TIMESLOT_LIST = (
        (0, "10:00"),
        (1, "11:00"),
        (2, "12:00"),
        (3, "13:00"),
        (4, "14:00"),
        (5, "15:00"),
        (6, "16:00"),
        (7, "17:00"),
        (8, "18:00"),
    )

    provider = models.ForeignKey(
        ProviderProfile,
        on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        CustomerProfile,
        on_delete=models.CASCADE
    )
    date = models.DateField(
        help_text="YYYY-MM-DD",
        default=datetime.now,
    )
    timeslot = models.IntegerField(
        choices=TIMESLOT_LIST
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
    )
