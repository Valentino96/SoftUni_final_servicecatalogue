from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from servicecatalogue.accounts.models import CustomerProfile, ProviderProfile

UserModel = get_user_model()


class CustomerCreateForm(auth_forms.UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name', 'age')

    def save(self, commit=True):
        user = super().save(commit=False)
        profile = CustomerProfile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            age=self.cleaned_data['age'],
            user=user,
        )
        user.is_customer = True
        user.save()
        if commit:
            profile.save()
        return user


class ProviderCreateForm(auth_forms.UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    job = forms.CharField()
    address = forms.CharField()
    phone_number = forms.IntegerField()

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name', 'job',  'address', 'phone_number')

    def save(self, commit=True):
        user = super().save(commit=False)
        profile = ProviderProfile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            job=self.cleaned_data['job'],
            address=self.cleaned_data['address'],
            phone_number=self.cleaned_data['phone_number'],
            user=user,
        )
        user.is_provider = True
        user.save()
        if commit:
            profile.save()
        return user


class CustomerEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = CustomerProfile
        fields = ('first_name', 'last_name', 'age')


class ProviderEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = ProviderProfile
        fields = ('first_name', 'last_name', 'job',  'address', 'phone_number')


class UserEditForm(auth_forms.UserChangeForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = UserModel
        fields = ('email', 'password', 'is_provider', 'is_customer', 'is_staff')


class UserCreateForm(auth_forms.UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ('email', )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
