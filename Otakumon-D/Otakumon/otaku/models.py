from django.db import models

# Create your models here.

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
    id = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length = 200)
    volumen = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    precio = models.IntegerField()
    
    def __str__(self):
        return self.nombre