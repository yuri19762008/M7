
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Producto , Fabricante
from .forms import ProductoForm, RegisterForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/producto_list.html'
    context_object_name = 'productos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos_por_fabricante'] = {}
        for fabricante in Fabricante.objects.all():
            context['productos_por_fabricante'][fabricante] = fabricante.productos.all()
        return context

class ProductoUpdateView(LoginRequiredMixin,UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'fabricante', 'f_vencimiento', 'pais']
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('producto-list')
    login_url = 'login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProductoDeleteView(LoginRequiredMixin,DeleteView):
    model = Producto
    template_name = 'productos/producto_confirm_delete.html'
    success_url = reverse_lazy('producto-list')
    login_url = 'login'

class ProductoCreateView(LoginRequiredMixin,CreateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'fabricante', 'f_vencimiento', 'pais']
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('producto-list')
    login_url = 'login'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Producto creado exitosamente')
        return response


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso. Por favor inicia sesión.')
        return super().form_valid(form)
    
class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'productos/producto_detail.html'
    context_object_name = 'producto'