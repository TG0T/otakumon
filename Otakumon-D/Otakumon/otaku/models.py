from django.db import models
from django.contrib.auth.models import User

#MODELOS BASE PARA DATOS DE LA PAGINA#

class Editorial(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.nombre
    
class Manga(models.Model):
    id = models.CharField(max_length=4, primary_key=True)
    portada = models.ImageField(upload_to='images/')
    nombre = models.CharField(max_length = 200)
    volumen = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()
    
    
    def __str__(self):
        return self.id

#MODELOS PARA EL CARRITO DE COMPRAS#

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    @property
    def subtotal(self):
        return self.manga.precio * self.cantidad
    

    def __str__(self):
        return f"{self.cantidad} x {self.manga.nombre}"

#BOLETA

class Boleta(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha_compra = models.DateField(auto_now_add=True)
    total_carrito = models.IntegerField()
    numero_boleta = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Boleta {self.numero_boleta}"


