class Usuario():
    def __init__(self, nome, email, data_nascimento, password):
        self.__nome = nome
        self.__email = email
        self.__data_nascimento = data_nascimento
        self.__password = password

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password