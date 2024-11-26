from django.db import models

# Create your models here.

class Socios(models.Model):
    Id_Socio = models.IntegerField(primary_key=True)
    nombre  = models.CharField(max_length=50)
    tipo_socio   = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    email =  models.EmailField(max_length=50)
    aporte  = models.CharField(max_length=100)
    beneficio = models.CharField(max_length=100)

    class Meta: 
        db_table =  "Socios"
        verbose_name = "Socio"
        verbose_name_plural = "Socios"

    def   __str__(self):
        return self.nombre