from django.contrib import admin

from .models import Animal, Pending


def make_published(modeladmin, request, queryset):
    for obj in queryset:
        animal = Animal(thai_name = obj.thai_name,
                        name = obj.name,
                        class_name = obj.class_name,
                        order = obj.order,
                        family = obj.family,
                        info = obj.info,
                        habitat = obj.habitat,
                        picture = obj.picture)
        animal.save()


make_published.short_description = "Published"

class PendingAdmin(admin.ModelAdmin):
    list_display = ['name', 'class_name']
    ordering = ['name']
    actions = [make_published]


admin.site.register(Animal)
admin.site.register(Pending, PendingAdmin)
