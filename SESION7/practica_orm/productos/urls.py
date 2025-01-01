
from django.urls import path
from .views import  ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView
from . import views

urlpatterns = [
    path('', ProductoListView.as_view(), name='producto-list'),
    path('crear/', ProductoCreateView.as_view(), name='producto-create'),
    path('producto/editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_update'),
    path('producto/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_eliminar'),
]

