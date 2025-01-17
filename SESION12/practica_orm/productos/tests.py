from django.test import TestCase, Client
from django.urls import reverse
from .models import Fabricante, Producto
from datetime import date

class ProductosTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear datos de prueba para Fabricante
        cls.fabricante = Fabricante.objects.create(
            nombre='P&G',
            pais='Estados Unidos'
        )
        
        # Crear datos de prueba para Producto
        cls.producto = Producto.objects.create(
            nombre='Protex Aloe',
            descripcion='Jabón antibacterial',
            precio=2500.00,
            fabricante=cls.fabricante,
            f_vencimiento=date(2025, 12, 31)
        )

    def test_model_content_fabrica(self):
        """Test 1: Verificar datos del modelo Fábrica"""
        fabricante = Fabricante.objects.get(id=self.fabricante.id)
        self.assertEqual(fabricante.nombre, 'P&G')
        self.assertEqual(fabricante.pais, 'Estados Unidos')

    def test_model_content_producto(self):
        """Test 2: Verificar datos del modelo Producto"""
        producto = Producto.objects.get(id=self.producto.id)
        self.assertEqual(producto.nombre, 'Protex Aloe')
        self.assertEqual(producto.fabricante.nombre, 'P&G')

    def test_url_producto(self):
        """Test 3: Verificar respuesta HTTP 200 de /producto/"""
        response = self.client.get(reverse('producto-list'))
        self.assertEqual(response.status_code, 200)

    def test_url_mostrar_pro(self):
        """Test 4: Verificar contenido de mostrar-pro"""
        # Primero crear un producto de prueba
        producto = self.producto  # Usar el producto creado en setUpTestData
        response = self.client.get(reverse('mostrar-pro', kwargs={'pk': producto.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'productos/producto_detail.html')
        self.assertContains(response, 'Información de Producto')


from django.test import TestCase, Client
from django.urls import reverse
from .models import Producto, Fabricante

class ProductoInsertarTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Crear datos de prueba
        self.fabricante = Fabricante.objects.create(
            nombre='P&G',
            pais='Estados Unidos'
        )

    def test_url_producto_insertar(self):
        """Test 1: Verificar URL /producto/insertar/"""
        response = self.client.get('/producto/crear/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'productos/producto_form.html')

    def test_url_insertar_pro_reverse(self):
        """Test 2: Verificar nombre de URL insertar-pro"""
        response = self.client.get(reverse('insertar-pro'))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        """Test 3: Verificar plantilla correcta"""
        response = self.client.get(reverse('insertar-pro'))
        self.assertTemplateUsed(response, 'productos/producto_form.html')

    def test_content_in_template(self):
        """Test 4: Verificar contenido específico en la plantilla"""
        response = self.client.get(reverse('insertar-pro'))
        self.assertContains(response, '<td>Nombre del Producto</td>')
