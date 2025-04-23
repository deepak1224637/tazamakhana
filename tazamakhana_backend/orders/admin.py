from django.contrib import admin

# Register your models here.
#from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity', 'created_at']
    list_filter = ['created_at', 'product']
    search_fields = ['user__username', 'product__name']
