from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', cursos),
    path('inicio/', inicio, name="inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('profesores/', profesores, name="Profesores"),
    path('setEstudiante/', setEstudiantes, name="setEstudiante"),
    path('getEstudiante/', getEstudiantes, name="getEstudiante"),
    path('buscarEstudiante/', buscarEstudiante, name="buscarEstudiante"),
    path('setProfesor/', setProfesores, name="setProfesor"),
    path('getProfesor/', getProfesores, name="getProfesor"),
    path('buscarProfesor/', buscarProfesor, name="buscarProfesor"),
    path('blogEstudiantes/', blog_estudiantes, name='Blog'),
    path('getCurso/', getCursos, name="getCurso"),
    path('buscarCurso/', buscarCurso, name="buscarCurso"),
    path('eliminarEstudiante/<nombre_estudiante>', eliminarEstudiante, name="eliminarEstudiante"),
    path('eliminarCurso/<nombre_curso>', eliminarCurso, name="eliminarCurso"),
    path('eliminarProfesor/<nombre_profesor>', eliminarProfesor, name="eliminarProfesor"),
    path('editarEstudiante/<nombre_estudiante>', editarEstudiante, name="editarEstudiante"),
    path('setCurso/', setCursos, name="setCurso"),
    path('editarCursos/<nombre_curso>', editarCurso, name="editarCurso"),
    path('editarProfesores/<nombre_profesor>', editarProfesor, name="editarProfesor"),
    path('Login/',loginWeb,name="Login"),
    path('registro/',registro,name="registro"),
    path('Logout/',LogoutView.as_view(template_name="AppCoder/Login.html"),name ='Logout'),
    path('Perfil/',perfilView,name="perfil"),
    path('Perfil/editarPerfil/',editarPerfil,name="editarPerfil"),
    path('Perfil/changePassword/',changePassword,name='changePassword'),
    path('Perfil/changeAvatar/', editAvatar, name="editAvatar"),

]