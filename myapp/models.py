from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Insignia(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    obtenida = models.BooleanField(default=False)
    imagen = models.ImageField()

class User(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    título = models.CharField(max_length=20)
    edad = models.SmallIntegerField()