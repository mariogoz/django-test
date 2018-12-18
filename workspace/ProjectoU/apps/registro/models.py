from django.db import models

# Create your models here.

class Registro(models.Model):
    rut = models.CharField(max_length=50)
    razon_social = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    listado_docuemento = models.IntegerField()
    fecha_registro = models.DateField()