from django.db import models

# Create your models here.
class Reserva(models.Model):

    id = models.AutoField(primary_key=True)
    nombre  = models.CharField(max_length=50)
    persoans = models.CharField(max_length=40)
    fechas= models.CharField(max_length=40)
    hora= models.CharField(max_length=40)
    celular= models.CharField(max_length=60)
    
    
    def __str__(self):
        return self.nombre

class domicilio(models.Model):

    id = models.AutoField(primary_key=True)
    
    nombre = models.CharField(max_length=40)
    direccion= models.CharField(max_length=60)
    telefono= models.CharField(max_length=60)
    
    
    def __str__(self):
        return self.nombre
