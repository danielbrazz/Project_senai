import ObjetoPedido
import os
clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP

pp = ObjetoPedido.Pedido("papel","100")
lista.append(pp)
gg = ObjetoPedido.Pedido("caneta","5")
lista.append(gg)

class Compras:
    def Main():
        clear()
        print("#######PERFIL Compras#######")
        print("1-Verificar/Modificar solicitações")
        print("5-Logout")
        r = input(": ")
        if int(r) == 1:
            Compras.Lista()
        elif int(r) == 5:
            return
        else:
            Compras.Main()

    def Lista():
        clear()
        for x in range(len(lista)): #para cada item na lista
           
            if int(lista[x].aprovGen) == 1 :
                print(str(x)+" "+"Item: "+lista[x].qtd+" "+lista[x].nome)
                if int(lista[x].aprovCom) == 2:
                    print("Aguardando verificação")
                elif int(lista[x].aprovCom) == 1:
                    print("Aprovado")
                else:
                    print("Negado")
                print("")

        h = 0
        for x in range(len(lista)):
            if int(lista[x].aprovGen) == 1 :
                y = input("Modificar item nº:")
                if x == int(y):
                    print(lista[x].qtd + " " +lista[x].nome)
                    r = input("Aprovar(1)   Reprovar(0)")
                    lista[x].aprovCom = r
                    h=h+1
                if  int(r) == 0:
                    lista[x].justificava=input('Motivo:')    

        if h == 0 :
            print("Aguardando requisições")  

        x = input("")
        Compras.Main()
