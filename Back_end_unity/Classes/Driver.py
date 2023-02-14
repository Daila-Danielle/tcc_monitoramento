
from pyModbusTCP.client import ModbusClient
cliente = ModbusClient('localhost',502,1,0.05)

class driver:
   def __init__(self):
      pass

   def Read(self,adress="%MW",len=1):
      
      if "%MW" in adress:
         addr=int(adress.removeprefix("%MW"))
         if cliente.open():
            read = cliente.read_holding_registers(addr,len) 
            cliente.close()
            return  read
         else:
            cliente.close()
            print("server não encontrado")
      else :
         if cliente.open():
               addr=int(adress.removeprefix("%M"))
               read = cliente.read_coils(addr,len) 
               cliente.close()
               return  read
         else:
               cliente.close()
               print("server não encontrado")

         

   def Write(self,adress="%MW",valores=[]):
         
      if "%MW" in adress:
         addr=int(adress.removeprefix("%MW"))

         if cliente.open():
            for x in range (len(valores)):
               cliente.write_multiple_registers(addr,valores) 
               cliente.close()  
         else:
            cliente.close()
            print("server não encontrado")
      else :
         if cliente.open():
            addr=int(adress.removeprefix("%M")) 
            for x in range (len(valores)):
               cliente.write_multiple_coils(addr,valores) 
               cliente.close()
         else:
            cliente.close()
            print("server não encontrado")




   


   
















        
   




