import ObjetoPedido
import os
clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP

pp = ObjetoPedido.Pedido("papel","100")
lista.append(pp)
gg = ObjetoPedido.Pedido("caneta","5")
lista.append(gg)

class Logistica:
    def Main():
        clear()
        print("#######PERFIL GERENCIAL#######")
        print("1-Verificar/Modificar solicitações")
        print("5-Logout")
        r = input(": ")
        if int(r) == 1:
            Logistica.Lista()
        elif int(r) == 5:
            return
        else:
            Logistica.Main()

    def Lista():
        clear()
        for x in range(len(lista)): #para cada item na lista
             if int(lista[x].aprovCom) == 1 :
                print(str(x)+" "+"Item: "+lista[x].qtd+" "+lista[x].nome)
                if int(lista[x].log) == 2:
                    print("Aguardando verificação")
                elif int(lista[x].log) == 1:
                    print("Recebido")
                else:
                    print("Recusado")

        h=0
        for x in range(len(lista)):
            if int(lista[x].aprovCom) == 1 :
                y = input("Modificar item nº:")
                if x == int(y):
                    print(lista[x].qtd + " " +lista[x].nome)
                    r = input("Recebido(1)   Recusado(0)")
                    lista[x].log = r
                    s = input("Foi entregue(1)  Em espera(0) ")
                    lista[x].entrega = s
                    h=h+1
        if h==0: 
            print("Aguardando Requisições")           
        x = input("")
        Logistica.Main()

