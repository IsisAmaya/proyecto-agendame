from django.db import models

# Create your models here.

class Freelancer(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nameFreelancer=models.CharField(max_length=300)
    servicios=models.CharField(max_length=250)
    image =models.ImageField(upload_to='freelancer/images/')
    ubicacion = models.CharField(max_length=250)
    disponibilidad = models.CharField(max_length=250)



