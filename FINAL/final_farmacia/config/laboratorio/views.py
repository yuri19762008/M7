from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Laboratorio, Producto, DirectorGeneral

#se agregan las clases para el laboratorio
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


#se agrega la clase para el producto

class ProductoListView(ListView):
    model = Producto
    template_name = 'producto/producto_list.html'
    context_object_name = 'productos'

class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'producto/producto_form.html'
    fields = ['nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta']
    success_url = reverse_lazy('producto_list')

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'producto/producto_form.html'
    fields = ['nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta']
    success_url = reverse_lazy('producto_list')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')

#se agrega la clase para el director general

class DirectorListView(ListView):
    model = DirectorGeneral
    template_name = 'director/director_list.html'
    context_object_name = 'directores'

class DirectorCreateView(CreateView):
    model = DirectorGeneral
    template_name = 'director/director_form.html'
    fields = ['nombre', 'laboratorio', 'especialidad']
    success_url = reverse_lazy('director_list')

class DirectorUpdateView(UpdateView):
    model = DirectorGeneral
    template_name = 'director/director_form.html'
    fields = ['nombre', 'laboratorio', 'especialidad']
    success_url = reverse_lazy('director_list')

class DirectorDeleteView(DeleteView):
    model = DirectorGeneral
    template_name = 'director/director_confirm_delete.html'
    success_url = reverse_lazy('director_list')

