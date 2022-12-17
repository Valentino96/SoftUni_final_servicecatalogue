from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from servicecatalogue.accounts.models import ProviderProfile

UserModel = get_user_model()

SERVICE_CHOICES = [
    ("Plumber", "Plumber"),
    ("Electrician", "Electrician"),
    ("Nail Artist", "Nail Artist"),
    ("Hair Dresser", "Hair Dresser"),
    ("Teacher", "Teacher"),
]


class Service(models.Model):
    MAX_LENGTH_TYPE = 30
    MAX_LENGTH_DESCRIPTION = 300
    MAX_LENGTH_LOCATION = 30

    type = models.CharField(
        max_length=MAX_LENGTH_TYPE,
        choices=SERVICE_CHOICES,
        default=None,
    )
    description = models.TextField(
        max_length=MAX_LENGTH_DESCRIPTION,
    )
    provider = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    location = models.CharField(
        max_length=MAX_LENGTH_LOCATION,
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.type}')
        return super().save(*args, **kwargs)


class ServiceComment(models.Model):
    MAX_TEXT_LENGTH = 300
    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


class ServiceLike(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


