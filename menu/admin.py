from django.contrib import admin
from .models import Menu,Shop,Category
# Register your models here.

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['shop','name']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name' , 'amount', 'image']




