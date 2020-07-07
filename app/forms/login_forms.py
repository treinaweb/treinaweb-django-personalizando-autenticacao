from django.contrib.auth.forms import AuthenticationForm
from django import forms
from ..models import Usuario


class LoginForm(AuthenticationForm):
    username = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['username', 'password']
