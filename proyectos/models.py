from django.db import models

# Create your models here.(representacion en codigo de una tabla)
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    url= models.CharField(max_length=100)
    
