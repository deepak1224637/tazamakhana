from django.contrib import admin

# Register your models here.
#from django.contrib import admin
from orders.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'state', 'postal_code']
    search_fields = ['user__username', 'city', 'state']
