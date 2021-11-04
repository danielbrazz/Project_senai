import ObjetoPedido
import os
clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP

#gg = ObjetoPedido.Pedido('papel','100')
#lista.append(gg)

class Compras:
    def Main():
        clear()
        print("#######PERFIL Compras#######")
        print("1-Verificar/Modificar solicitações")
        print("5-Logout")
        r = input(": ")
        if int(r) == 1:
            Compras.Lista()
            Compras.Main()
        elif int(r) == 5:
            return
        else:
            Compras.Main()

    def Lista():
        clear()
        h = 0
        print("pressione '0' para sair")
        print("")
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
                h=h+1

        if h == 0 :
            print("Aguardando requisições") 
            f = input('')
            return
        else:
            y = input("Modificar item nº:")
            d = int(y)-1 #numero certo
            if int(y) == 0:
                return
            for x in range(len(lista)):
                if int(lista[x].aprovGen) == 1 :
                    if x == d:
                        print(lista[x].qtd + " " +lista[x].nome)
                        r = input("Aprovar(1)   Reprovar(0)")
                        if r == 's':
                            Compras.Main() 
                        if  int(r) == 0:
                            lista[x].justificava=input('Motivo:')                      
                        if int(r) == 0 or int(r) == 1:
                            lista[x].aprovCom = r 
                        else:
                            print("input incorreto")
                            x = input("")
                            Compras.Lista()                    
        Compras.Lista()
