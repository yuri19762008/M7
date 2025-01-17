from django.urls import path
from .views import LaboratorioListView, LaboratorioCreateView, LaboratorioUpdateView, LaboratorioDeleteView

urlpatterns = [
    path('', LaboratorioListView.as_view(), name='laboratorio_list'),
    path('create/', LaboratorioCreateView.as_view(), name='laboratorio_create'),
    path('update/<int:pk>/', LaboratorioUpdateView.as_view(), name='laboratorio_update'),
    path('delete/<int:pk>/', LaboratorioDeleteView.as_view(), name='laboratorio_delete'),
]
