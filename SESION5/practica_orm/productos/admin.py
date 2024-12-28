
# Register your models here.
from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'precio', 'fabricante')
    list_filter = ('precio',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('id',)
