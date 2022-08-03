from typing import List
from cliente import Cliente
from view.cadastro import Cadastro
from view.cores import Cores
from view.home import Home

from view.login import Login
from models.status_resposta import StatusResposta
from models.usuario import Usuario

home:Home = Home()
login:Login = Login()
cadastro:Cadastro=Cadastro()
opLogin=1
cores=Cores()
def preencherUsuarios(usuarios:List[Usuario]):
    for usuario in usuarios:
        usuario.moveis = login.buscarMoveis(usuario.cpf)
        usuario.propostasFeitas = login.buscarPropostasRealizadas(usuario.cpf)
        usuario.propostasRecebidas = login.buscarPropostasRecebidas(usuario.cpf)
while opLogin!=0:
    usuarios = Cliente().buscarTodosUsuarios()
    preencherUsuarios(usuarios)
    opLogin=login.menu()
    if opLogin == 1:
        usuario = login.login()
        if usuario is not None:
            print(cores.criarTextoSucesso("\nLogin realizado com sucesso!"))
            print(cores.criarTextoSucesso("Seja bem-vindo(a) {}.\n".format(usuario.nome)))
            opHome = home.menu()
            while opHome != 0:
                usuarios = Cliente().buscarTodosUsuarios()
                preencherUsuarios(usuarios)
                usuario.moveis = login.buscarMoveis(usuario.cpf)
                usuario.propostasFeitas = login.buscarPropostasRealizadas(usuario.cpf)
                usuario.propostasRecebidas = login.buscarPropostasRecebidas(usuario.cpf)
                if opHome == 1:
                    home.mostrarMoveis(usuario.moveis)
                elif opHome == 2:
                    status=home.cadastrarMovel(cpf=usuario.cpf)
                    if status == StatusResposta.sucesso.value:
                        print(cores.criarTextoSucesso("Cadastro do móvel realizado com sucesso!"))
                    else:
                        print(cores.criarTextoErro("Cadastro do móvel não pôde ser realizado com sucesso!"))
                    print()
                    
                elif opHome == 3:
                    status=home.excluirMovel(usuario.cpf)
                    if status == StatusResposta.sucesso.value:
                        print(cores.criarTextoSucesso("Móvel excluído com sucesso!"))
                    else:
                        print(cores.criarTextoErro("Móvel não pôde ser excluído com sucesso!"))
                    print()
        
                elif opHome == 4:
                    home.mostrarPropostasRealizadas(usuario.propostasFeitas)
                elif opHome == 5:
                    home.mostrarPropostasRecebidas(usuario.propostasRecebidas)
                elif opHome == 6:
                    home.aceitarProposta(usuario.cpf)                  
                elif opHome == 7:
                    home.recusarProposta(usuario.cpf)
                elif opHome == 8:
                    home.mostrarMoveisDisponiveisEscambo(usuarios,usuario.cpf)
                elif opHome == 9:
                    home.fazerProposta(usuario.cpf,usuarios=usuarios)
                opHome = home.menu()
        else:
            print(cores.criarTextoErro("\nLogin não pôde ser realizado com sucesso!\n"))
    
    elif opLogin == 2:
        status = cadastro.menu()
        if status == StatusResposta.sucesso.value:
            print(cores.criarTextoSucesso("Cadastro realizado com sucesso!"))
        else:
            print(cores.criarTextoErro("Cadastro não pôde ser realizado com sucesso!"))
        print()
print(cores.criarTextoTela("---------- FIM TELA DE LOGIN ----------"))