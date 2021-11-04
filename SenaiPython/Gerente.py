import ObjetoPedido
import os
clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP

class Gerente:
    def Main():
        clear()
        print("#######PERFIL GERENCIAL#######")
        print("1-Verificar/Modificar solicitações")
        print("5-Logout")
        r = input(": ")
        if int(r) == 1:
            Gerente.Lista()
            Gerente.Main()
        elif int(r) == 5:
            return
        else:
            Gerente.Main()

    def Lista():
        clear()
        h = 0
        print("presione '0' para sair")
        for x in range(len(lista)): #para cada item na lista
            print(str(x+1)+" "+"Item: "+lista[x].qtd+" "+lista[x].nome)
            if int(lista[x].aprovGen) == 2:
                print("Aguardando verificação")
            elif int(lista[x].aprovGen) == 1:
                print("Aprovado")
            else:
                print("Negado")
            print("")
            h = h+1

        if h == 0 :
            print("Aguardando requisições") 
            f = input('')
            return
        else:
            y = input("Modificar item nº:")
            d = int(y)-1 #numero certo
            if int(y) == 0:
                return
            else:
                for x in range(len(lista)):
                    if x == d:
                        print(lista[x].qtd + " " +lista[x].nome)
                        r = input("Aprovar(1)   Reprovar(0)")
                        if r == 's':
                            Gerente.Main()            
                        elif  int(r) == 0:
                            lista[x].justificava=input('Motivo:')             
                            lista[x].aprovGen = r
                        elif int(r) == 1:
                            lista[x].aprovGen = r 
                        else:
                            print("input incorreto")
                            x = input("")
                            Gerente.Lista()
        Gerente.Lista()
