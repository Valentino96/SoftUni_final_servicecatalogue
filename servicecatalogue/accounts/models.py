from django.db import models
from django.contrib.auth import models as auth_models

from servicecatalogue.accounts.managers import AppUserManager


class ApplicationUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )
    is_customer = models.BooleanField(
        null=False,
        blank=False,
        default=False,
    )
    is_provider = models.BooleanField(
        null=False,
        blank=False,
        default=False,
    )
    is_staff = models.BooleanField(default=False)
    # valentino@abv.bg
    # kJKwaE7VarxNJfd
    USERNAME_FIELD = 'email'

    objects = AppUserManager()


class CustomerProfile(models.Model):
    first_name = models.CharField(
        max_length=25
    )
    last_name = models.CharField(
        max_length=25
    )
    age = models.PositiveIntegerField()

    user = models.OneToOneField(
        ApplicationUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )


class ProviderProfile(models.Model):
    first_name = models.CharField(
        max_length=30
    )
    last_name = models.CharField(
        max_length=30,
    )
    job = models.CharField(
        max_length=30,
    )
    address = models.CharField(
        max_length=35,
    )
    phone_number = models.PositiveIntegerField(
        null=False,
        blank=False,
    )
    user = models.OneToOneField(
        ApplicationUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )


