from django.db import models

from django.contrib.auth.models import AbstractUser

# creacion de fabricantes
class Fabricante(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    
# creacion de productos
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, related_name='productos')
    f_vencimiento = models.DateField(null=True, blank=True)
    pais = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.fabricante.nombre}"
    

# creacion de usuario personalizado
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    class Meta:
        permissions = [
            ("can_view_products", "Can view products"),
            ("can_edit_products", "Can edit products"),
        ]

    # Especificar related_name únicos para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )
