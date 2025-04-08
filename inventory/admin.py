from django.contrib import admin
from .models import Category
from .models import Product
from .models import Cart

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    pass

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass
