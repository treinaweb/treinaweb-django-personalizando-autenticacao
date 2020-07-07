from ..models import Usuario

def cadastrar_usuario(usuario):
    Usuario.objects.create_user(nome=usuario.nome, email=usuario.email, data_nascimento=usuario.data_nascimento,
                                password=usuario.password)