from django.db import models
from django.contrib.auth.models import User

class Estudiante(models.Model):
    def __str__(self):
        return f"nombre:{self.nombre} - apellido:{self.apellido} - email:{self.email}"
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Profesor(models.Model):
    def __str__(self):
        return f"nombre:{self.nombre} - apellido:{self.apellido} - email:{self.email}"
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Curso(models.Model):
    def __str__(self):
        return f"nombre:{self.nombre} - camada:{self.camada} - horario:{self.horario}"
    nombre = models.CharField(max_length=30)
    camada = models.CharField(max_length=30)
    horario = models.CharField(max_length=30)

class Entregable(models.Model):
    def __str__(self):
        return f"curso:{self.curso} - fecha:{self.fecha} - entregada:{self.entregada}"
    curso = models.CharField(max_length=30)
    fecha = models.CharField(max_length=30)
    entregada = models.BooleanField()

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null = True, blank = True)