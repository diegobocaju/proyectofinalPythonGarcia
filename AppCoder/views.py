from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from AppCoder.models import *
from AppCoder.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User


@login_required
def inicio(request):
    avatar = getavatar(request)
    return render(request, "AppCoder/inicio.html", {"avatar": avatar})


def cursos(request):
    Cursos = Curso.objects.all()
    return render(request, "AppCoder/cursos.html",{"Cursos": Cursos})

@login_required
def profesores(request):
    Profesores = Profesor.objects.all()
    return render(request, "AppCoder/profesores.html",{"Profesores": Profesores})

@login_required
def estudiantes(request):
    Estudiantes = Estudiante.objects.all()
    return render(request, "AppCoder/estudiantes.html", {"Estudiantes": Estudiantes})

@login_required
def entregables(request):
    Entregables = Entregable.objects.all()
    return render(request, "AppCoder/entregables.html",{"Entregables": Entregables})

@user_passes_test(lambda u: u.is_superuser)
@login_required
def setEstudiantes(request):
    Estudiantes = Estudiante.objects.all()
    if request.method == 'POST':
        miFormulario1 = formSetEstudiante(request.POST)
        if miFormulario1.is_valid():
            data = miFormulario1.cleaned_data
            estudiante = Estudiante(nombre=data["nombre"], apellido=data["apellido"], email=data["email"])    
            estudiante.save()
            miFormulario1 = formSetEstudiante()
            return render(request, "AppCoder/setEstudiantes.html", {'miFormulario1': miFormulario1, 'Estudiantes': Estudiantes})
    else:
        miFormulario1 = formSetEstudiante()
    return render(request, "AppCoder/setEstudiantes.html", {'miFormulario1': miFormulario1,'Estudiantes': Estudiantes})

@user_passes_test(lambda u: u.is_superuser)
@login_required
def getEstudiantes(request):
    return render(request, "AppCoder/getEstudiantes.html")

@user_passes_test(lambda u: u.is_superuser)
@login_required
def buscarEstudiante(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        estudiantes = Estudiante.objects.filter(nombre = nombre)
        return render(request, "AppCoder/getEstudiantes.html", {"estudiantes":estudiantes})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def setProfesores(request):
    Profesores = Profesor.objects.all()
    if request.method == 'POST':
        miFormulario2 = formSetProfesor(request.POST)
        print(miFormulario2)
        if miFormulario2.is_valid:
            data = miFormulario2.cleaned_data
            profesor = Profesor(nombre=data["nombre"],apellido=data["apellido"], email=data["email"])    
            profesor.save()
            miFormulario2 = formSetProfesor()
            return render(request,"AppCoder/setProfesores.html", {"miFormulario2":miFormulario2, "Profesores":Profesores}) 
    else:
        miFormulario2 = formSetProfesor()
    return render(request, "AppCoder/setProfesores.html", {"miFormulario2":miFormulario2, "Profesores":Profesores})

@user_passes_test(lambda u: u.is_superuser)
@login_required
def getProfesores(request):
    return render(request, "AppCoder/getProfesores.html")

@user_passes_test(lambda u: u.is_superuser)
@login_required
def buscarProfesor(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        profesores = Profesor.objects.filter(nombre = nombre)
        return render(request, "AppCoder/getProfesores.html", {"profesores":profesores})
    else:
        respuesta = "Sin datos"
    
    return HttpResponse(respuesta)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def setCursos(request):
    Cursos = Curso.objects.all()
    miFormulario3 = formSetCurso()
    if request.method == 'POST':
        miFormulario3 = formSetCurso(request.POST)
        print(miFormulario3)
        if miFormulario3.is_valid():
            data = miFormulario3.cleaned_data
            curso = Curso(nombre=data["nombre"],camada=data["camada"], horario=data["horario"])    
            curso.save()
            miFormulario3 = formSetCurso()
            return render(request,"AppCoder/setCursos.html", {"miFormulario3":miFormulario3, "cursos":Cursos})    
    else:
        miFormulario3 = formSetCurso()
    return render(request, "AppCoder/setCursos.html", {"miFormulario3":miFormulario3, "cursos":Cursos})

@login_required
def getCursos(request):
    return render(request, "AppCoder/getCursos.html")

@login_required
def buscarCurso(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre = nombre)
        return render(request, "AppCoder/getCursos.html", {"cursos":cursos})
    else:
        respuesta = "Sin datos"
    
    return HttpResponse(respuesta)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def setEntregables(request):
    Entregables = Entregable.objects.all()
    if request.method == 'POST':
        miFormulario4 = formSetEntregable(request.POST)
        print(miFormulario4)
        if miFormulario4.is_valid():
            data = miFormulario4.cleaned_data
            entregable = Entregable(curso=data["curso"], fecha=data["fecha"], entregada=data["entregada"])    
            entregable.save()
            miFormulario4 = formSetEntregable()
            return render(request, "AppCoder/setEntregables.html", {"miFormulario4": miFormulario4, "Entregables": Entregables})
    else:
        miFormulario4 = formSetEntregable()
    return render(request, "AppCoder/setEntregables.html", {"miFormulario4": miFormulario4, "Entregables": Entregables})

@login_required
def getEntregables(request):
    return render(request, "AppCoder/getEntregables.html")

@login_required
def buscarEntregable(request):
    if request.GET["curso"]:
        curso = request.GET["curso"]
        entregables = Entregable.objects.filter(curso = curso)
        return render(request, "AppCoder/getEntregables.html", {"entregables":entregables})
    else:
        respuesta = "Sin datos"
    
    return HttpResponse(respuesta)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def eliminarEstudiante(request, nombre_estudiante):
    estudiante = Estudiante.objects.get(nombre= nombre_estudiante)
    estudiante.delete()
    miFormulario1 = formSetEstudiante()
    Estudiantes = Estudiante.objects.all()
    return render (request, "AppCoder/setEstudiantes.html",{'miFormulario1': miFormulario1, 'Estudiantes': Estudiantes})

@user_passes_test(lambda u: u.is_superuser)
@login_required
def eliminarCurso(request, nombre_curso):
    curso = Curso.objects.get(nombre= nombre_curso)
    curso.delete()
    miFormulario3 = formSetCurso()
    Cursos = Curso.objects.all()
    return render (request, "AppCoder/setCursos.html",{'miFormulario3': miFormulario3, 'Cursos': Cursos})

@user_passes_test(lambda u: u.is_superuser)
@login_required
def eliminarProfesor(request, nombre_profesor):
    profesor = Profesor.objects.get(nombre= nombre_profesor)
    profesor.delete()
    miFormulario2 = formSetProfesor()
    Profesores = Profesor.objects.all()
    return render (request, "AppCoder/setProfesores.html",{'miFormulario2': miFormulario2, 'Profesor': Profesores})

@user_passes_test(lambda u: u.is_superuser)
@login_required
def eliminarEntregable(request, curso_entregable):
    entregable = Entregable.objects.get(curso= curso_entregable)
    entregable.delete()
    miFormulario4 = formSetEntregable()
    Entregables= Entregable.objects.all()
    return render (request, "AppCoder/setEntregables.html",{'miFormulario2': miFormulario4, 'Entregables': Entregables})

@user_passes_test(lambda u: u.is_superuser)
@login_required
def editarEstudiante(request, nombre_estudiante):
    estudiante = Estudiante.objects.get(nombre=nombre_estudiante)
    if request.method == 'POST':
        miFormulario1 = formSetEstudiante(request.POST)
        if miFormulario1.is_valid():
            data = miFormulario1.cleaned_data
            estudiante.nombre = data['nombre']
            estudiante.apellido = data['apellido']
            estudiante.email = data['email']
            estudiante.save()
            miFormulario1 = formSetEstudiante()
            Estudiantes = Estudiante.objects.all()
            return render(request, "AppCoder/setEstudiantes.html", {"miFormulario1": miFormulario1, "Estudiantes": Estudiantes})
    
    miFormulario1 = formSetEstudiante(initial={'nombre': estudiante.nombre, 'apellido': estudiante.apellido, 'email': estudiante.email})
    return render(request, "AppCoder/editarEstudiantes.html", {"miFormulario1": miFormulario1})

@user_passes_test(lambda u: u.is_superuser)
@login_required
def editarCurso(request, nombre_curso):
    curso = Curso.objects.get(nombre=nombre_curso)
    if request.method == 'POST':
        miFormulario3 = formSetCurso(request.POST)
        if miFormulario3.is_valid():
            data = miFormulario3.cleaned_data
            curso.nombre = data['nombre']
            curso.camada = data['camada']
            curso.horario = data['horario']
            curso.save()
            miFormulario3 = formSetCurso()
            Cursos = Curso.objects.all()
            return render(request, "AppCoder/setCursos.html", {"miFormulario3": miFormulario3, "Cursos": Cursos})
    
    miFormulario3 = formSetCurso(initial={'nombre': curso.nombre, 'camada': curso.camada, 'horario': curso.horario})
    return render(request, "AppCoder/editarCursos.html", {"miFormulario3": miFormulario3})

@user_passes_test(lambda u: u.is_superuser)
@login_required
def editarProfesor(request, nombre_profesor):
    profesor = Profesor.objects.get(nombre=nombre_profesor)
    if request.method == 'POST':
        miFormulario2 = formSetProfesor(request.POST)
        if miFormulario2.is_valid():
            data = miFormulario2.cleaned_data
            profesor.nombre = data['nombre']
            profesor.apellido = data['apellido']
            profesor.email = data['email']
            profesor.save()
            miFormulario2 = formSetProfesor()
            Profesores = Profesor.objects.all()
            return render(request, "AppCoder/setProfesores.html", {"miFormulario2": miFormulario2, "Profesores": Profesores})
    
    miFormulario2 = formSetProfesor(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email': profesor.email})
    return render(request, "AppCoder/editarProfesores.html", {"miFormulario2": miFormulario2})

@user_passes_test(lambda u: u.is_superuser)
@login_required
def editarEntregable(request, curso_entregable):
    entregable = Entregable.objects.get(curso=curso_entregable)
    if request.method == 'POST':
        miFormulario4 = formSetEntregable(request.POST)
        if miFormulario4.is_valid():
            data = miFormulario4.cleaned_data
            entregable.curso = data['curso']
            entregable.fecha = data['fecha']
            entregable.entregada = data['entregada']
            entregable.save()
            miFormulario4 = formSetEntregable()
            Entregables = Entregable.objects.all()
            return render(request, "AppCoder/setEntregables.html", {"miFormulario4": miFormulario4, "Entregables": Entregables})
    
    miFormulario4 = formSetEntregable(initial={'curso': entregable.curso, 'fecha': entregable.fecha, 'entregada': entregable.entregada})
    return render(request, "AppCoder/editarEntregables.html", {"miFormulario4": miFormulario4})


def loginWeb(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['user'],password=request.POST['password'])
        if user is not None:
            login(request,user)
            return render(request,"AppCoder/inicio.html")
        else:
            return render(render,"AppCoder/Login.html",{'error':'Usuario y/o contraseña incorrecta'})
    else:
        return render(request,'AppCoder/Login.html')

def registro(request):
    if request.method == 'POST':
        userCreate = UserCreationForm(request.POST)
        if userCreate is not None:
            userCreate.save()
            return render(request,"AppCoder/Login.html")
    else:
        return render(request,"AppCoder/registro.html")

@login_required
def perfilView(request):
    return render(request, 'AppCoder/Perfil/Perfil.html')

@login_required  
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'AppCoder/Perfil/Perfil.html')
    else:
        form = UserEditForm(initial= {'username': usuario.username, 'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name })
        return render(request, 'AppCoder/Perfil/editarPerfil.html', {"form": form})

@login_required
def changePassword(request):
    usuario = request.user 
    if request.method =="POST":
        form = ChangePasswordForm(data = request.POST, user = usuario)
        if form.is_valid():
            if  request.POST['new_password1'] == request.POST['new_password2']:
                user = form.save()
                update_session_auth_hash(request, user)
            return HttpResponse('Passwords do not match')
        return render(request, 'AppCoder/inicio.html')
    else:
        form= ChangePasswordForm(user = usuario)
        return render(request, 'AppCoder/Perfil/changePassword.html', {"form": form})
    
def editAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, "AppCoder/inicio.html", {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarForm()
        except:
            form = AvatarForm()
    return render(request, "AppCoder/Perfil/avatar.html", {'form': form})

def getavatar(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar

    

