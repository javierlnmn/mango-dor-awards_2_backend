from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name")
    search_fields = ("username", "first_name", "last_name")
    list_filter = ("is_staff", "is_superuser", "is_active")
