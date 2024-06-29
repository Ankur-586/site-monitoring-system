from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from django.contrib.sessions.models import Session

class UserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'full_name', 'is_staff', 'is_superuser', 'is_active']
    search_fields = ['email', 'username', 'first_name', 'last_name']
    readonly_fields = ['date_joined']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )

    ordering = ['email']
    filter_horizontal = ()

    def full_name(self, obj):
        return obj.full_name

    full_name.short_description = 'Full Name'

# Register the CustomUser model with the UserAdmin class
admin.site.register(CustomUser, UserAdmin)

admin.site.register(Session)