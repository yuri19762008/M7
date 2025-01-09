from django.db import models

class PrecioHistoricoVehiculos(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    modelo = models.TextField()
    precio = models.DecimalField(
        null=False,
        decimal_places=2,
        max_digits=10)
    
    color = models.CharField(
        max_length=50, 
        default="Desconocido")
    
    
