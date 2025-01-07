from django.urls import path
from . import views

urlpatterns = [
    path('username/<str:cadena>/', views.mostrar_cadena, name='mostrar_cadena'),
]
