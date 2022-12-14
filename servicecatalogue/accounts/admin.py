from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from servicecatalogue.accounts.forms import UserEditForm, UserCreateForm
from servicecatalogue.accounts.models import CustomerProfile, ProviderProfile

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    form = UserEditForm
    add_form = UserCreateForm
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('is_customer', 'is_provider')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    def get_form(self, request, obj=None, **kwargs):
        return super().get_form(request, obj, **kwargs)


@admin.register(CustomerProfile)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(ProviderProfile)
class ProviderAdmin(admin.ModelAdmin):
    pass
