from django.contrib import admin

from .models import Candidate, CandidateImage, Gender, Nationality


class CandidateImageInline(admin.TabularInline):
    model = CandidateImage
    extra = 1


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'gender', 'nationalities')
    search_fields = ('first_name', 'last_name', 'age', 'gender', 'nationalities')
    list_filter = (
        'first_name',
        'last_name',
        'age',
        'gender',
    )
    prepopulated_fields = {'slug': ('first_name', 'last_name')}

    inlines = [CandidateImageInline]

    def get_nationalities(self, obj):
        return ', '.join(obj.nationalities)

    get_nationalities.short_description = 'Nationalities'


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    list_filter = ('code', 'name')


@admin.register(Nationality)
class NationalityAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    list_filter = ('code', 'name')
