
# Register your models here.
from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'precio', 'fabricante','pais', 'f_vencimiento')
    list_filter = ('precio','fabricante')
    search_fields = ('nombre', 'descripcion')
    ordering = ('id',)
