from django.db import models

class Fabricante(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, related_name='productos')
    f_vencimiento = models.DateField(null=True, blank=True)
    pais = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.fabricante.nombre}"
    
