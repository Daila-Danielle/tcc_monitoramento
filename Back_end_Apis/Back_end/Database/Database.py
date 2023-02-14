#blibiotecas
import mysql.connector
import pyodbc 

# classe para o banco de dados
class DB :
    # variaves para conexão e querys
    def __init__(self,Debug=False,Source={}):
        self._host = Source['host']
        self._user = Source['user']
        self._senha = Source['password']
        self._database = Source['database']
        self._id = Source['id']

        self._debug = Debug

        self.query = "Vazio"
        self.rowcount = 0
        self.erro =("Sem Erro")
     
    #funcão para executar uma query do tipo DML,DDL
    def execute(self,sql,valores):
        self.query = "Vazio"
        self.erro =("Sem Erro")

        if self._id == 1:
            DBcon = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ self._host 
            +';DATABASE='+ self._database
            +';ENCRYPT='+self._encrypt
            +';UID='+self._user
            +';PWD='+  self._senha)
            
            cursor = DBcon.cursor()
            
        elif self._id == 2:

            DBcon = mysql.connector.connect(
            host = self._host,
            database = self._database,
            user = self._user,
            password= self._senha )

            cursor = DBcon.cursor()

        try:
            cursor.execute(sql,valores)
            DBcon.commit()
            self.query = cursor.fetchall()
            self.rowcount = cursor.rowcount
            cursor.close
            DBcon.close

        except Exception as er:
            self.erro = er
            DBcon.close

        if self._debug:
            print("Query_Executada:",sql,valores)
            print("Query_RowCount:",self.rowcount)
            print("Query_Resultado:",self.query)
            print("Query_Erro:",self.erro)



    #funcão para executar uma query do tipo DQL (select)
    def execute_select(self,sql,valores=0):
        self.query = "Vazio"
        self.erro =("Sem Erro")

        if self._id == 1:
            DBcon = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ self._host 
            +';DATABASE='+ self._database
            +';ENCRYPT='+self._encrypt
            +';UID='+self._user
            +';PWD='+  self._senha)
            
            cursor = DBcon.cursor()
            
        elif self._id == 2:

            DBcon = mysql.connector.connect(
            host = self._host,
            database = self._database,
            user = self._user,
            password= self._senha
            )
            cursor = DBcon.cursor()

        try:
            if valores == 0:
                 
                cursor.execute(sql)
                self.query = cursor.fetchall()
                self.rowcount = cursor.rowcount
                cursor.close
                DBcon.close
            else:
               
                cursor.execute(sql,valores)
                self.query = cursor.fetchall()
                self.rowcount = cursor.rowcount
                cursor.close
                DBcon.close

        except Exception as er:
            self.erro = er  
            DBcon.close

        if self._debug:
            print("Query_Executada:",sql,valores)
            print("Query_RowCount:",self.rowcount)
            print("Query_Resultado:",self.query)
            print("Query_Erro:",self.erro)