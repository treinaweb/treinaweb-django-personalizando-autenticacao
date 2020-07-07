from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from .manager import UsuarioManager

# Create your models here.

class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ("A", "Alta"),
        ("N", "Normal"),
        ("B", "Baixa"),
    ]
    titulo = models.CharField(max_length=30, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    data_expiracao = models.DateField(null=False, blank=False)
    prioridade = models.CharField(max_length=1, choices=PRIORIDADE_CHOICES, null=False, blank=False)

class Usuario(AbstractBaseUser):
    objects = UsuarioManager()

    nome = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    data_nascimento = models.DateField(null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'data_nascimento']
