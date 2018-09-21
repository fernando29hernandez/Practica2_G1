from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Seccion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return 'Id:{} Nombre:{}'.format(self.id,self.nombre)

class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='Articulo')
    seccion_fk = models.ForeignKey(Seccion,on_delete=models.CASCADE)
    def __str__(self):
        return '{} {}'.format(self.id,self.nombre)

class Usuario(AbstractUser):
    tipo = models.BooleanField(default=False)     
    def __str__(self):     	
        return '{} {}'.format(self.id,self.username)

class Carrito(models.Model):
    usuario_fk = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    monto_a_pagar = models.IntegerField(null=True)
class Detalle_Carrito(models.Model):
    carrito_fk = models.ForeignKey(Carrito,on_delete=models.CASCADE)
    articulo_fk = models.ForeignKey(Articulo,on_delete=models.CASCADE)
    cantidad_articulos = models.IntegerField()

class Factura(models.Model):
    usuario_fk = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=3000)

