from django.db import models
from django.contrib.auth import models as auth_models
from django.core import validators

from servicecatalogue.accounts.managers import AppUserManager
from servicecatalogue.core.modelsvalidators import validate_is_letters_only


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

    USERNAME_FIELD = 'email'

    objects = AppUserManager()


class CustomerProfile(models.Model):
    MAX_LENGTH_NAME = 25
    MIN_LENGTH_NAME = 2

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_NAME),
            validate_is_letters_only,
        )
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_NAME),
            validate_is_letters_only,
        )
    )
    age = models.PositiveIntegerField()

    user = models.OneToOneField(
        ApplicationUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ProviderProfile(models.Model):
    MAX_LENGTH_NAME = 25
    MIN_LENGTH_NAME = 2
    MAX_LENGTH_ADDRESS = 35
    MAX_LENGTH_JOB = 15

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_NAME),
            validate_is_letters_only,
        )
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_NAME),
            validate_is_letters_only,
        )
    )
    job = models.CharField(
        max_length=MAX_LENGTH_JOB,
    )
    address = models.CharField(
        max_length=MAX_LENGTH_ADDRESS,
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

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


