import ObjetoPedido
import os
clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP

pp = ObjetoPedido.Pedido("papel","100")
lista.append(pp)
gg = ObjetoPedido.Pedido("caneta","5")
lista.append(gg)

class Gerente:
    def Main():
        clear()
        print("#######PERFIL GERENCIAL#######")
        print("1-Verificar/Modificar solicitações")
        print("5-Logout")
        r = input(": ")
        if int(r) == 1:
            Gerente.Lista()
        elif int(r) == 5:
            return
        else:
            Gerente.Main()

    def Lista():
        clear()
        for x in range(len(lista)): #para cada item na lista
            print(str(x)+" "+"Item: "+lista[x].qtd+" "+lista[x].nome)
            if int(lista[x].aprovGen) == 2:
                print("Aguardando verificação")
            elif int(lista[x].aprovGen) == 1:
                print("Aprovado")
            else:
                print("Negado")
            print("")

        y = input("Modificar item nº:")
        for x in range(len(lista)):
            if x == int(y):
                print(lista[x].qtd + " " +lista[x].nome)
                r = input("Aprovar(1)   Reprovar(0)")
                lista[x].aprovGen = r
        
        x = input("")
        Gerente.Main()
