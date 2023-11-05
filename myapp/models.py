from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Insignia(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    obtenida = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title + ' - ' + self.project.name

class User(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    título = models.CharField(max_length=20)
    edad = models.SmallIntegerField()