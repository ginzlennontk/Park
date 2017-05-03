from django.contrib import admin

from .models import Animal


def make_published(modeladmin, request, queryset):
    queryset.update(status='Published')


make_published.short_description = "Published"

class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name', 'class_name', 'status']
    ordering = ['name']
    actions = [make_published]


admin.site.register(Animal, AnimalAdmin)
