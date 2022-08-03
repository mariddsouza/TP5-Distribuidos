from ast import List
import json
import requests
from models.movel import Movel
from models.proposta import Proposta

from models.usuario import Usuario
class Cliente:
   def __init__(self) -> None:
      self.host ="http://127.0.0.1:5000"
       
   def criarUsuario(self,usuario:Usuario)-> int:
      try:
         response = requests.get(self.host+"/usuario/cadastrar", data= json.dumps(
               {
            "nome":usuario.nome,
            "cpf": usuario.cpf,
            "senha": usuario.senha,
          }))
         response = response.json()
         return response['status']
      except Exception as e:
         
         return None
          
   def buscarUsuario(self,cpf:int,senha:str)-> Usuario:
      try:
         response = requests.get(self.host+"/login", data= json.dumps(
            {
         "cpf": cpf,
         "senha": senha,
         }))
         response=response.json()
         return Usuario(nome=response['nome'],cpf=response['cpf'],senha=response['senha'])
      except Exception as e:
            
            return None
   
   def buscarTodosUsuarios(self)-> list:
      try:
         response = requests.get(self.host+"/usuarios")
         response=response.json()
         usuarios = []
         for v in response.values():
            usuarios.append(Usuario(nome=v['nome'],cpf=v['cpf'],senha=v['senha']))
         return usuarios
      except Exception as e :
         
         return None
      
   def cadastrarMovel(self,cpf:int, movel:Movel)-> int:
      try:
         response = requests.get(self.host+"/movel/cadastrar", data= json.dumps(
               {
            "nome":movel.nome,
            "descricao": movel.descricao,
            "tempoUso": movel.tempoUso,
            "cpf": cpf
         }))
         response = response.json()
         return response['status']
      except Exception as e:
         
         return None
   
   def excluirMovel(self,idMovel:int,cpf:int)-> int:
      try:
         response = requests.get(self.host+"/movel/excluir", data= json.dumps(
               {
            "idMovel":idMovel,
            "cpf": cpf,
         }))
         response=response.json()
         return response['status']
      except Exception as e:
         
         return None
   
   def buscarMoveis(self,cpf:int):
      try:
         response = requests.get(self.host+"/moveis",data=json.dumps(
            {
               'cpf':cpf
            }
         ))
         response=response.json()
         moveis = []
         for v in response.values():
            moveis.append(Movel(nome=v['nome'],tempoUso=v['tempoUso'],descricao=v['descricao'],id=v['id']))
         return moveis
      except Exception as e :
         
         return None
         
   def buscarPropostasRealizadas(self,cpf:int):
      try:
         response = requests.get(self.host+"/propostas-realizadas",data=json.dumps(
            {
               'cpf':cpf
            }
         ))
         response=response.json()
         propostas = []
            
         for proposta in response.values():
            userAlvo = proposta['usuarioAlvo']
            userRequisitante = proposta['usuarioRequisitante']
            movelProposto = proposta['movelProposto']
            movelRequerido = proposta['movelRequerido']

            usuarioAlvo = Usuario(nome=userAlvo['nome'],cpf=userAlvo['cpf'],senha=userAlvo['senha'],
               moveis=[],propostasFeitas=[],propostasRecebidas=[])

            usuarioRequisitante = Usuario(nome=userRequisitante['nome'],
            cpf=userRequisitante['cpf'],senha=userRequisitante['senha'],
               moveis=[],propostasFeitas=[],propostasRecebidas=[])

            movelProposto =Movel(nome=movelProposto['nome'],tempoUso=movelProposto['tempoUso'],id=movelProposto['id'],
            descricao=movelProposto['descricao'])

            movelRequerido =Movel(nome=movelRequerido['nome'],tempoUso=movelRequerido['tempoUso'],id=movelRequerido['id'],
            descricao=movelRequerido['descricao'])

            propostas.append(Proposta(idProposta=proposta['id'],usuarioAlvo=usuarioAlvo,usuarioRequisitante=usuarioRequisitante
            ,movelProposto=movelProposto,movelRequerido=movelRequerido,status=proposta['status']))

         return propostas
      except Exception as e :
         
         return None
   
   def buscarPropostasRecebidas(self,cpf:int):
      try:
         response = requests.get(self.host+"/propostas-recebidas",data=json.dumps(
            {
               'cpf':cpf
            }
         ))
         response=response.json()
         propostas = []
            
         for proposta in response.values():
            userAlvo = proposta['usuarioAlvo']
            userRequisitante = proposta['usuarioRequisitante']
            movelProposto = proposta['movelProposto']
            movelRequerido = proposta['movelRequerido']

            usuarioAlvo = Usuario(nome=userAlvo['nome'],cpf=userAlvo['cpf'],senha=userAlvo['senha'],
               moveis=[],propostasFeitas=[],propostasRecebidas=[])

            usuarioRequisitante = Usuario(nome=userRequisitante['nome'],
            cpf=userRequisitante['cpf'],senha=userRequisitante['senha'],
               moveis=[],propostasFeitas=[],propostasRecebidas=[])

            movelProposto =Movel(nome=movelProposto['nome'],tempoUso=movelProposto['tempoUso'],id=movelProposto['id'],
            descricao=movelProposto['descricao'])

            movelRequerido =Movel(nome=movelRequerido['nome'],tempoUso=movelRequerido['tempoUso'],id=movelRequerido['id'],
            descricao=movelRequerido['descricao'])

            propostas.append(Proposta(idProposta=proposta['id'],usuarioAlvo=usuarioAlvo,usuarioRequisitante=usuarioRequisitante
            ,movelProposto=movelProposto,movelRequerido=movelRequerido,status=proposta['status']))

         return propostas
      except Exception as e :

         return None
   
   
   def aceitarProposta(self,idProposta:int,cpfUsuario:int):
      try:
         response = requests.get(self.host+"/aceitar-proposta",data=json.dumps(
            {
               'idProposta':idProposta,
               "cpfUsuario":cpfUsuario
            }
         ))
         response = response.json()
         return response['status']
      except Exception as e:
         
         return None

   def recusarProposta(self,idProposta:int,cpfUsuario:int):
      try:
         response = requests.get(self.host+"/recusar-proposta",data=json.dumps(
            {
               'idProposta':idProposta,
               "cpfUsuario":cpfUsuario
            }
         ))
         response = response.json()
         return response['status']
      except Exception as e:
         
         return None
 
   def fazerProposta(self,cpfRequisitante:int,idMovelRequerido:int,idMovelProposto:int,
      cpfRequisitado:int):
      try:
         response = requests.get(self.host+"/proposta/criar",data=json.dumps(
            {
               'cpfRequisitante':cpfRequisitante,
               "idMovelRequerido":idMovelRequerido,
               'idMovelProposto':idMovelProposto,
               'cpfRequisitado':cpfRequisitado
            }
         ))
         response = response.json()
         return response['status']
      except Exception as e:
         
         return None
    
 

