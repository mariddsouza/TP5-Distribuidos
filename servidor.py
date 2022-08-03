import json
from banco.cadastro import *
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/login")    
def login():
    try:
        requisicao = json.loads(request.data)
        usuario:Usuario = buscarUsuarioBanco(cpf=requisicao["cpf"],senha=requisicao["senha"])
        dic = {
            "nome" : usuario.nome,
            "cpf": usuario.cpf,
            "senha": usuario.senha,
        }
        return jsonify(dic)
    except Exception as e:
        print(e)
        return None
@app.route("/usuario/cadastrar")
def cadastrarUsuario():
    requisicao = json.loads(request.data)
    usuario:Usuario =Usuario(nome=requisicao['nome'],cpf=requisicao['cpf'],senha=requisicao['senha'])
    status=inserirUsuario(usuario)
    return  jsonify({'status': status})

@app.route("/usuarios")
def getTodosUsuarios():
        usuarios = listarUsuarios()
        cont = 0
        users = {}
        for usuario in usuarios:
            users[str(cont)]={
            "nome" : usuario.nome,
            "cpf": str(usuario.cpf),
            "senha": usuario.senha,
        }   
            cont+=1
        return jsonify(users)

@app.route("/movel/cadastrar")
def criarMovel():
    requisicao = json.loads(request.data)
    movel:Movel =Movel(nome=requisicao['nome'],tempoUso=requisicao['tempoUso'],descricao=requisicao['descricao'])
    status=inserirMovel(requisicao["cpf"], movel)
    return  jsonify({'status': status})
@app.route("/movel/excluir")
def excluirMovel():
    requisicao = json.loads(request.data)
    status= deletarMovel(idMovel=requisicao['idMovel'],cpf=requisicao['cpf'])
    return jsonify({'status':status})

@app.route("/moveis")
def getMoveis():
    requisicao = json.loads(request.data)
    moveis = buscarMoveis(cpf=requisicao["cpf"])
    cont = 0
    furnitures = {}
    for movel in moveis:
        furnitures[str(cont)]={
        "nome" : movel.nome,
        "id": str(movel.id),
        "tempoUso":movel.tempoUso,
        "descricao": movel.descricao
        }   
        cont+=1
    return jsonify(furnitures)


@app.route("/propostas-realizadas")
def getPropostasRealizadas():
    requisicao = json.loads(request.data)
    propostas =  buscaPropostaRealizada(requisicao['cpf'])
    cont = 0
    response = {}
    for proposta in propostas:
        response[str(cont)]={
            "id":int(proposta.idProposta),
            "usuarioAlvo":{
            "nome" : proposta.usuarioAlvo.nome,
            "senha": proposta.usuarioAlvo.senha,
            "cpf": proposta.usuarioAlvo.cpf,
            },
            "usuarioRequisitante":{
            "nome" : proposta.usuarioRequisitante.nome,
            "senha": proposta.usuarioRequisitante.senha,
            "cpf": proposta.usuarioRequisitante.cpf,
            },
            "movelProposto":{
                "nome" : proposta.movelProposto.nome,
            "id": str(proposta.movelProposto.id),
            "tempoUso":int(proposta.movelProposto.tempoUso),
            "descricao": proposta.movelProposto.descricao
            },
             "movelRequerido":{
                "nome" : proposta.movelRequerido.nome,
            "id": str(proposta.movelRequerido.id),
            "tempoUso":int(proposta.movelRequerido.tempoUso),
            "descricao": proposta.movelRequerido.descricao
            },
            "status": proposta.status
            }
    return jsonify(response)

@app.route("/propostas-recebidas")
def getPropostasRecebidas():
    requisicao = json.loads(request.data)
    propostas =  buscaPropostaRecebida(requisicao['cpf'])
    cont = 0
    response = {}
    for proposta in propostas:
        response[str(cont)]={
            "id":int(proposta.idProposta),
            "usuarioAlvo":{
            "nome" : proposta.usuarioAlvo.nome,
            "senha": proposta.usuarioAlvo.senha,
            "cpf": proposta.usuarioAlvo.cpf,
            },
            "usuarioRequisitante":{
            "nome" : proposta.usuarioRequisitante.nome,
            "senha": proposta.usuarioRequisitante.senha,
            "cpf": proposta.usuarioRequisitante.cpf,
            },
            "movelProposto":{
                "nome" : proposta.movelProposto.nome,
            "id": str(proposta.movelProposto.id),
            "tempoUso":int(proposta.movelProposto.tempoUso),
            "descricao": proposta.movelProposto.descricao
            },
             "movelRequerido":{
                "nome" : proposta.movelRequerido.nome,
            "id": str(proposta.movelRequerido.id),
            "tempoUso":int(proposta.movelRequerido.tempoUso),
            "descricao": proposta.movelRequerido.descricao
            },
            "status": proposta.status
            }
    return jsonify(response)

@app.route("/aceitar-proposta")
def aceitarPropsota():
    requisicao = json.loads(request.data)
    status=aceitaProposta(requisicao['idProposta'],cpfUsuarioAlvo=requisicao['cpfUsuario'])
    return jsonify({"status": status})

@app.route("/recusar-proposta")
def recusarPropsota():
    requisicao = json.loads(request.data)
    status=recusaProposta(requisicao['idProposta'],cpfUsuarioAlvo=requisicao['cpfUsuario'])
    return jsonify({"status": status})

@app.route("/proposta/criar")
def fazerProposta():
    requisicao = json.loads(request.data)
    status=criarProposta(requisicao['idMovelRequerido'], requisicao['idMovelProposto'],
            requisicao['cpfRequisitante'], requisicao['cpfRequisitado'])
    return jsonify({"status":status})
if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000)