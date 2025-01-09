from django.urls import path
from .views import index, agregar, agregarregistro, eliminar, actualizar, actualizarregistro

urlpatterns = [
    path("", index, name="index"),
    path("agregar/", agregar, name ="agregar"),
    path("agregar/agregarregistro/", agregarregistro , name ="agregarregistro"),
    path("eliminar/<int:id>", eliminar, name = "eliminar"),
    path("actualizar/<int:id>", actualizar, name = "actualizar"),
    path("actualizarregistro/<int:id>", actualizarregistro, name = "actualizarregistro"),

]