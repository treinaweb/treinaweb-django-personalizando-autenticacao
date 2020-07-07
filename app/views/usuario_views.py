from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from ..forms.usuario_forms import UsuarioForm
from ..entidades.usuario import Usuario


def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UsuarioForm(data=request.POST)
        if form_usuario.is_valid():
            nome = form_usuario.cleaned_data["nome"]
            email = form_usuario.cleaned_data["email"]
            data_nascimento = form_usuario.cleaned_data["data_nascimento"]
            password1 = form_usuario.cleaned_data["password1"]
            usuario_novo = Usuario(nome=nome, email=email, data_nascimento=data_nascimento, password=password1)
            return redirect('listar_tarefas')
    else:
        form_usuario = UsuarioForm()
    return render(request, 'usuarios/form_usuario.html', {"form_usuario": form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('listar_tarefas')
        else:
            messages.error(request, 'As credenciais estão incorretas')
            return redirect('logar_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuarios/login.html', {"form_login": form_login})

def deslogar_usuario(request):
    logout(request)
    return redirect('logar_usuario')