from django.contrib import admin

from .models import Category, Vote


class VoteInline(admin.TabularInline):
    model = Vote
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    list_filter = ('name', 'code')
    exclude = ('winner',)
    prepopulated_fields = {'slug': ('name',)}

    inlines = [VoteInline]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'candidate', 'category', 'points')
    search_fields = ('user', 'candidate', 'category', 'points')
    list_filter = ('user', 'candidate', 'category', 'points')
