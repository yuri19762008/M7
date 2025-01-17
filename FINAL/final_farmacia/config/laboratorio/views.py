from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Laboratorio

class LaboratorioListView(ListView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_list.html'

class LaboratorioCreateView(CreateView):
    model = Laboratorio
    fields = ['nombre', 'ciudad', 'pais']
    template_name = 'laboratorio/laboratorio_form.html'
    success_url = reverse_lazy('laboratorio_list')

class LaboratorioUpdateView(UpdateView):
    model = Laboratorio
    fields = ['nombre', 'ciudad', 'pais']
    template_name = 'laboratorio/laboratorio_form.html'
    success_url = reverse_lazy('laboratorio_list')

class LaboratorioDeleteView(DeleteView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_confirm_delete.html'
    success_url = reverse_lazy('laboratorio_list')
