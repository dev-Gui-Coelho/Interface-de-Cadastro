class User:
    def __init__(self, nome:str = None, email:str = None, num:str = None, senha:str = None) -> None:
        self.__nome = nome
        self.__email = email
        self.__num = num
        self.__gen = None
        self.__pais = None
        self.__senha = senha
    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, n):
        self.__nome = n

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, e):
        self.__email = e

    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, n):
        self.__num = n

    @property
    def gen(self):
        return self.__gen
    @gen.setter
    def gen(self, g):
        self.__gen = g
    
    @property
    def pais(self):
        return self.__pais
    @pais.setter
    def pais(self, p):
        self.__pais = p

    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, s):
        self.__senha = s

    def cripto_senha(self):
        pass

    def __str__(self) -> str:
        return f'---------------------DADOS------------------------\nNome: {self.__nome}\nEmail: {self.__email}\nNúmero p/ Contato: {self.__num}\nGênero: {self.__gen}\nPaís: {self.__pais}\nSenha: {self.__senha}'

