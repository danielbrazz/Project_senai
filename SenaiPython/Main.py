#Main
from Operario import Operario  
from Gerente import Gerente
from Compras import Compras
from Logistica import Logistica
import os
clear = lambda: os.system('cls')
 
class Menu:
    def inicio():
        clear()
        print("#######SELECIONE CONTA#######")
        print("1-Operario")
        print("2-Gerente")
        print("3-Compras")
        print("4-Logistica")
        print("9-Sair")
        r = input(": ")

        if int(r) == 1:
            Operario.Main()
        elif int(r) == 2:
            Gerente.Main()
        elif int(r) == 3:
            Compras.Main()
            #script compras
        elif int(r) == 4:
            Logistica.Main()
        elif int(r) == 9:
            return
        else:
            Menu.inicio()
        Menu.inicio()
      
Menu.inicio()
