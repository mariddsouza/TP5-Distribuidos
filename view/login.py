from typing import List
from cliente import Cliente


from view.cores import Cores
from models.movel import Movel
from models.proposta import Proposta
from models.status_resposta import StatusResposta
from models.usuario import Usuario


class Login:
    def __init__(self,) -> None:
        pass
    def menu(self)->int:
        cores = Cores()
        print(cores.criarTextoTela("---------- TELA DE LOGIN ----------"))
        print()
        print("---- Bem-vindo ao Escamo ----")
        print("Escolha uma opção:")
        print(cores.criarTextoOpcoes("0")+" - Encerrar do sistema")
        print(cores.criarTextoOpcoes("1")+" - Entrar no sistema")
        print(cores.criarTextoOpcoes("2")+" - Cadastrar no sistema")
        opcao=int(input(cores.criarTextoEntrada("Opção: ")))
        print()
        return opcao

    def login(self)->Usuario:
        cores = Cores()
        cliente = Cliente()
        cpf=int(input(cores.criarTextoOpcoes("Insira seu CPF: ")))
        senha=input(cores.criarTextoOpcoes("Insira sua senha: "))
        usuario = cliente.buscarUsuario(cpf=cpf,senha=senha)
        print(cores.criarTextoTela("---------- FIM TELA DE LOGIN ----------"))
        return usuario
        
    def buscarMoveis(self,cpf:int)->List[Movel]:
        cliente =Cliente()
        return cliente.buscarMoveis(cpf)
    
    def buscarPropostasRealizadas(self,cpf:int)->List[Proposta]:
        cliente =Cliente()
        return cliente.buscarPropostasRealizadas(cpf)

    def buscarPropostasRecebidas(self,cpf:int)->List[Proposta]:
        cliente =Cliente()
        return cliente.buscarPropostasRecebidas(cpf)
        

        

