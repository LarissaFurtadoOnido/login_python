from .Cadastro import Cadastro

class Login(Cadastro):
    def __init__(self, usuario, senha):
        super().__init__(usuario, senha)
    
    def verificacao(self, entrada_usuario:str, entrada_senha:str):
        if entrada_usuario !=  self.__usuario or entrada_senha != self.__senha:
           print("Usuário ou senha  incorretos!")

