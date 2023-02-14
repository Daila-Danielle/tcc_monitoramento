from Classes.Driver import driver
from Classes.Tempos import Timer

Driver = driver()
Ton1 = Timer()


while(1):
    Ton1.Ton(0.5)
    lista=[0,1,0,1]

    if Ton1.Q:
        Driver.Write("%M100",lista)
        print("##############################")
        print("##############################")
        print("##############################")
        print(Driver.Read("%M100",4))