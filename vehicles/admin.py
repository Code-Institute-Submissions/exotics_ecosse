from django.contrib import admin
from .models import Vehicle, Category

# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Category, CategoryAdmin)

