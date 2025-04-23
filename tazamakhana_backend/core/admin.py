#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product

# Register your models here.
#admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'preview_image']
    list_filter = ['price']
    search_fields = ['name', 'description']
    readonly_fields = ['preview_image']
    
    def preview_image(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="70" height="70" />'
        return "-"
    preview_image.allow_tags = True
    preview_image.short_description = 'Image'
