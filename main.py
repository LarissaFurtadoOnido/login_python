from src.Cadastro import Cadastro
from src.Login import Login

if __name__ == "__main__":

    opcao = int(input("Já possui cadastro? 1-Sim 2-Não"))
    if opcao == 1:
        login = Login

        entrada_usuario = input("Usuário: ")
        entrada_senha = input("Senha: ")
        
        login.verificacao(entrada_usuario, entrada_senha)
    
    else:
        cadastro = Cadastro
        usuario = input("Usuário: ")
        senha = input("Senha: ")
    

        

    

    


