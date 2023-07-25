from django import forms
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from AppCoder.models import *
class formSetEstudiante(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

    def __str__(self):
        return self.titulo

class formSetProfesor (forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class formSetCurso (forms.Form):
    nombre = forms.CharField(max_length=30)
    camada = forms.CharField(max_length=30)
    horario = forms.CharField(max_length=30)


class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Email"}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"First Name"}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Last Name"}))
    password = None


    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name'] #'password'
        help_texts = {k:"" for k in fields}


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label = "", widget=forms.PasswordInput(attrs={"placeholder":"Old Password"}))
    new_password1 = forms.CharField(label = "", widget=forms.PasswordInput(attrs={"placeholder":"New Password"}))
    new_password2 = forms.CharField(label = "", widget=forms.PasswordInput(attrs={"placeholder":"Confirm New Password"}))
    

    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']
        help_texts ={k:"" for k in fields}

class AvatarForm(forms.Form):
    avatar = forms.ImageField()

class FormAnotarseCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada', 'horario']

class EntradaBlogForm(forms.ModelForm):
    class Meta:
        model = EntradaBlog
        fields = ['titulo', 'contenido']

