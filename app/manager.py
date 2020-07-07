from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, data_nascimento, password):
        if not email:
            raise ValueError("O usuário precisa de um email")
        usuario = self.model(
            nome = nome,
            data_nascimento = data_nascimento,
            email = self.normalize_email(email)
        )
        usuario.set_password(password)
        usuario.save()
        return usuario