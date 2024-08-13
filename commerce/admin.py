from django.contrib import admin
from .models import Product, Cart, Cartitems

# Register your models here.

class ContactProduct(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'status']
    list_filter = ['status']
    

admin.site.register(Product, ContactProduct)
admin.site.register(Cart)
admin.site.register(Cartitems)

# Register your models here.
