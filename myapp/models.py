from django.db import models
from django.contrib.auth.models import User

# Create your models here



class Insignia(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    obtenida = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='files/')
    portador = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title

class User(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    título = models.CharField(max_length=20)
    edad = models.SmallIntegerField()

class UserInsignias(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    insignia_id = models.ForeignKey(Insignia, on_delete=models.CASCADE)