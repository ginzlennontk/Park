from django.contrib import admin

from .models import Animal, AnimalImage


def make_published(modeladmin, request, queryset):
    queryset.update(status='Published')


make_published.short_description = "Published"


class AnimalImageInline(admin.TabularInline):
    model = AnimalImage

class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name', 'class_name', 'status']
    ordering = ['name']
    actions = [make_published]
    inlines = [
        AnimalImageInline,
    ]



admin.site.register(Animal, AnimalAdmin)
