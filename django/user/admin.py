from django.contrib import admin
from user.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'created_at', 'updated_at',
                    'is_active', 'is_staff', 'is_superuser')


admin.site.register(CustomUser, CustomUserAdmin)
