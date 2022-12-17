from django.core.exceptions import ValidationError


def validate_is_letters_only(value):
    for letters in value:
        if not letters.isalpha():
            raise ValidationError('Only letters are allowed')