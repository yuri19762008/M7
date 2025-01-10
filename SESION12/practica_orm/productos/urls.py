
from django.urls import path,include
from .views import  ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView, RegisterView, ProductoDetailView
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', ProductoListView.as_view(), name='producto-list'),
    path('crear/', ProductoCreateView.as_view(), name='producto-create'),
    path('producto/editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_update'),
    path('producto/eliminar/<int:pk>/', ProductoDeleteView.as_view(),name='producto_eliminar'),
    path('registro/', RegisterView.as_view(), name='registro'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
]
