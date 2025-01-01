from django.contrib import admin
from .models import Fabricante, Producto

@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    search_fields = ('nombre', 'pais')
    ordering = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'f_vencimiento', 'fabricante')
    list_filter = ('fabricante', 'f_vencimiento')
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)
