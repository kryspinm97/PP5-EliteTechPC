from django.contrib import admin
from .models import Category, PrebuiltPC

# Register your models here.


class ProductAdmin(admin.ModelAdmin):

    """ Admin configuration for the PrebuiltPC model """

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

    """ Admin configuration for the Category model """

    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(PrebuiltPC, ProductAdmin)
