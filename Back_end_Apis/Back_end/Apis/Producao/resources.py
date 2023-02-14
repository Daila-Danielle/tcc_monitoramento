#blibiotecas
from flask_restx import Resource
from flask import request
import time
from Database.Database import DB

#inporta configuraçao do banco de dados arquivo config
from Database.Config import Db_source

#Inicializa a isstancia do bando de dados
Database = DB(Debug=True,Source=Db_source())

#pega os segundos para gerar o id da produção
seconds = int(time.time())
Curent_prodID = 0

# API Produçao
class Producao (Resource):

    #metodo POST
    def post(self):

        global Curent_prodID

        initial_date = request.json["initial_date"]
        Curent_prodID = seconds
        
        values = (Curent_prodID,initial_date)
        sql= "insert into producao (id,initial_date)values(%s,%s)"
        
        Database.execute(sql,values)

        return 'Producao iniciada com sucesso',201
        pass

    #metodo PUT
    def put(self):

        global Curent_prodID

        id = Curent_prodID
        final_date = request.json["final_date"]
       
        valores=(id,)
        sql= "SELECT id FROM producao WHERE id = %s"
        Database.execute_select (sql,valores)
        
        if Database.rowcount >= 1 :

            valores = (final_date,Curent_prodID)
            sql = "UPDATE production SET final_date = %s WHERE producao.id = %s"

            Database.execute(sql,valores)
            Curent_prodID = 0

            return "Producao Fechada Com Sucesso",200
        else:
            return "Nenhuma Producao foi iniciada",404
  
    #metodo DELETE
    def delete(self):
        id = request.json ['id']

        values=(id,)    
        sql = "DELETE FROM materiais_producao WHERE id_prod = %s"
        Database.execute(sql,values)
        sql = "DELETE FROM producao WHERE id_prod = %s"
        Database.execute(sql,values)
        
        return "Producao Deletada com sucesso",201   