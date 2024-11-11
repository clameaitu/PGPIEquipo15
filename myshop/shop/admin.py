from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug', 'precio',
                    'disponible', 'creado', 'actualizado']
    list_filter = ['disponible', 'creado', 'actualizado']
    list_editable = ['precio', 'disponible']
    prepopulated_fields = {'slug': ('nombre',)}