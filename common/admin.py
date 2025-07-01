from django.contrib import admin

from .models import SiteParameters


@admin.register(SiteParameters)
class SiteParametersAdmin(admin.ModelAdmin):
    list_display = ("winners_reveal_date",)
    search_fields = ("winners_reveal_date",)
    list_filter = ("winners_reveal_date",)
