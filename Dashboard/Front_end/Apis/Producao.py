# blibiotecas 
import requests
import json
# importa o link do arquivo de confuguraçao 
from .Apis_config import APIServer_Name

#API para buscar dados das produçoes
def get_Production():
    dados = requests.get(APIServer_Name['Producao'])
    return json.loads(dados.content)
        
#API para iniciar uma produção    
def post_Production(date):
    values = {
        "initial_date":date           
    }
    resposta = requests.post(APIServer_Name['Producao'],json=values) 
    print(resposta)
    print(resposta.text)
        
#API para Finalizar uma produção 
def put_Production(date):
    values = {
        "final_date":date           
    }
    resposta = requests.put(APIServer_Name['Producao'],json=values) 
    print(resposta)
    print(resposta.text)
        
#API para Deletar uma produção     
def delete_Production(id):
    values = {
        "id":id           
    }
    resposta = requests.delete(APIServer_Name['Producao'],json=values) 
    print(resposta)
    print(resposta.text)   
   