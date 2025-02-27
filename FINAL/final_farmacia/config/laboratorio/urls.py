from django.urls import path
from .views import LaboratorioListView, LaboratorioCreateView, LaboratorioUpdateView, LaboratorioDeleteView, ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView, DirectorListView, DirectorCreateView, DirectorUpdateView, DirectorDeleteView, HomeView

urlpatterns = [
    #se agrega la url para el home
    path('', HomeView.as_view(), name='home'),
    
    #se agregan las urls para el laboratorio
    path('laboratorios', LaboratorioListView.as_view(), name='laboratorio_list'),
    path('create/', LaboratorioCreateView.as_view(), name='laboratorio_create'),
    path('update/<int:pk>/', LaboratorioUpdateView.as_view(), name='laboratorio_update'),
    path('delete/<int:pk>/', LaboratorioDeleteView.as_view(), name='laboratorio_delete'),
    
    #se agregan las urls para el producto
    path('productos/', ProductoListView.as_view(), name='producto_list'),
    path('productos/crear/', ProductoCreateView.as_view(), name='producto_create'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_update'),
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto_delete'),
    
    #se agregan las urls para el director general
    path('directores/', DirectorListView.as_view(), name='director_list'),
    path('directores/crear/', DirectorCreateView.as_view(), name='director_create'),
    path('directores/<int:pk>/editar/', DirectorUpdateView.as_view(), name='director_update'),
    path('directores/<int:pk>/eliminar/', DirectorDeleteView.as_view(), name='director_delete'),
]
