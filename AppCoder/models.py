from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Curso(models.Model):
    def __str__(self):
        return f"nombre:{self.nombre} - camada:{self.camada} - horario:{self.horario}"
    nombre = models.CharField(max_length=30)
    camada = models.CharField(max_length=30)
    horario = models.CharField(max_length=30)

class Horario(models.Model):
    def __str__(self):
        return self.horario
    curso = models.ForeignKey(Curso, related_name='horarios', on_delete=models.CASCADE)
    horario = models.CharField(max_length=100)

class Estudiante(models.Model):
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.email}"    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cursos = models.ManyToManyField(Curso, through='Inscripcion', related_name='estudiantes')


class EntradaBlog(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Inscripcion(models.Model):
    def __str__(self):
        return f"{self.estudiante} - {self.curso} - {self.horario}"
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    horario = models.CharField(max_length=100)


class Profesor(models.Model):
    def __str__(self):
        return f"nombre:{self.nombre} - apellido:{self.apellido} - email:{self.email}"
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null = True, blank = True)

