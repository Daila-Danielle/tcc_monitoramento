#blibiotecas
from flask_restx import Resource
from flask import request
from Database.Database import DB

#inporta configuraçao do banco de dados arquivo config
from Database.Config import Db_source

#Inicializa a isstancia do bando de dados
Database = DB(Debug=True,Source=Db_source())

# API Dados cadastro
class Dados_Producao (Resource):
    #metodo GET
    def get(self):

        dt_inicial=request.args.get('dt_inicial')
        dt_final=request.args.get('dt_final')
        
        lista=[]
        if dt_inicial == '' and dt_final == '':
            sql ="SELECT tb1.id_prod,tb1.initial_date,tb1.final_date,SUM(tb2.quantidade) FROM producao tb1 INNER JOIN materiais_producao tb2 on tb1.id_prod = tb2.id_prod GROUP BY tb1.id_prod" 
            Database.execute_select(sql)
        else : 
            valores=(dt_inicial.replace("T"," "),dt_final.replace("T"," "))  
            sql ="SELECT tb1.id_prod,tb1.initial_date,tb1.final_date,SUM(tb2.quantidade) FROM producao tb1 INNER JOIN materiais_producao tb2 on tb1.id_prod = tb2.id_prod WHERE tb1.initial_date >= %s AND tb1.final_date <= %s GROUP BY tb1.id_prod"
            Database.execute_select(sql,valores)
       
        for row in Database.query:
            dict={}
            dict={  
                    "id_prod":row[0],
                    "total":str(row[3]),
                    "inicio":str(row[1]),
                    "fim":str(row[2])                       
            }
            lista.append(dict)
    
        return lista
    

class Dados_Producao_Detalhar(Resource):
    #metodo GET
    def get(self):

        prod_id=request.args.get('prod_id')
        valores=(prod_id,)
        lista=[]
        sql ="SELECT tb1.id_prod, tb1.id_mat, tb1.quantidade, tb2.nome, tb3.nome FROM materiais_producao tb1 INNER JOIN materiais tb2 INNER JOIN mat_tipo tb3 ON tb2.id_mat = tb1.id_mat AND tb2.tipo_id = tb3.tipo_id WHERE tb1.id_prod = %s" 
     
        Database.execute_select(sql,valores)
        for row in Database.query:
            dict={}
            dict={  
                    "id_prod":row[0],
                    "id_mat":row[1],
                    "nome":row[3],
                    "qtd":row[2],
                    "tipo":row[4]                       
            }
            lista.append(dict)
    
        return lista