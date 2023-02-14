#blibiotecas
from flask_restx import Resource
from flask import request
from Database.Database import DB

#inporta configuraçao do banco de dados arquivo config
from Database.Config import Db_source

#Inicializa a isstancia do bando de dados
Database = DB(Debug=True,Source=Db_source())

#API Login
class Login (Resource):
    
    #metodo POST
    def post( self):

        nome = request.json["nome"]
        valores=(nome,)

        sql= "SELECT senha FROM usuarios WHERE binary nome like %s"
        Database.execute_select (sql,valores)

        if (Database.rowcount > 0):
            hash = Database.query[0][0]
            return hash,201
        else:
            return "",204
       

