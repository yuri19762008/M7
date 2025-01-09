from django.db import models
import datetime

annos_choices = [] 
for r in range(1950, (datetime.datetime.now().year+1)): 
   annos_choices.append((r,r)) 

def anno_actual(): 
   return datetime.date.today().year 



class Automotriz(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.CharField(max_length=255, default ="Chile")

    def __str__(self):
        return self.nombre

class DirectorEjecutivo(models.Model):
    automotriz = models.OneToOneField(Automotriz, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre

class TipoCombustible(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class ModeloCarro(models.Model):
    nombre = models.CharField(max_length=255)
    
    automotriz = models.ForeignKey(Automotriz,
                    on_delete=models.SET_NULL,
                    blank=True,
                    null=True)
    
    tipo_combustible = models.ManyToManyField(TipoCombustible, related_name="modelo_carros")

    f_fabricacion = models.IntegerField(choices=annos_choices, default=anno_actual) 
    costo_fabricacion = models.DecimalField(null=False, decimal_places=2, max_digits=10, default = 0) 
    precio_venta = models.DecimalField(null=False, decimal_places=2, max_digits=10, default = 0)

    def __str__(self):
        return self.nombre

