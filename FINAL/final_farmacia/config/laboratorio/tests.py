from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Lab Test",
            ciudad="Ciudad Test",
            pais="País Test"
        )

    def test_laboratorio_content(self):
        self.assertEqual(self.laboratorio.nombre, "Lab Test")
        self.assertEqual(self.laboratorio.ciudad, "Ciudad Test")
        self.assertEqual(self.laboratorio.pais, "País Test")

    def test_laboratorio_list_view(self):
        response = self.client.get(reverse('laboratorio_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lab Test")
        self.assertTemplateUsed(response, 'laboratorio/laboratorio_list.html')

    def test_laboratorio_detail_view(self):
        response = self.client.get(reverse('laboratorio_update', args=[self.laboratorio.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lab Test")
        self.assertTemplateUsed(response, 'laboratorio/laboratorio_form.html')
