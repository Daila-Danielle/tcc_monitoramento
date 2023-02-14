#blibiotecas
from flask_restx import Resource
from flask import request
from Database.Database import DB

#inporta configuraçao do banco de dados arquivo config
from Database.Config import Db_source

#Inicializa a isstancia do bando de dados
Database = DB(Debug=True,Source=Db_source())

# API Dados cadastro
class Dados_Cadastro (Resource):
    
    #metodo GET
    def get( self):
        
        sql ="SELECT tb1.id_prod,tb1.initial_date,tb1.final_date,SUM(tb2.quantidade) FROM producao tb1 INNER JOIN materiais_producao tb2 on tb1.id_prod = tb2.id_prod GROUP BY tb1.id_prod" 
        valores =(1,)
        Database.execute_select(sql)
        print(Database.query)

        lista=[]
        sql ="select nome,id from cargos " 
        Database.execute_select(sql)
        Database.query = [tuple(row) for row in Database.query]

        dict={}
        dict={  
                "cargos":Database.query    
        }
        lista.append(dict)
        
        sql ="select nome,id from grupos " 
        Database.execute_select(sql)
        Database.query = [tuple(row) for row in Database.query]
       
        dict={}
        dict={  
                "grupos":Database.query          
        }

        lista.append(dict)
        return lista