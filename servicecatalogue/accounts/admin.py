from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from servicecatalogue.accounts.models import CustomerProfile, ProviderProfile

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    list_display = ('email', )
    ordering = ('-email',)
    list_filter = ('email', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_customer', 'is_provider',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', )})
    )


@admin.register(CustomerProfile)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(ProviderProfile)
class ProviderAdmin(admin.ModelAdmin):
    pass
