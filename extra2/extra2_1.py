def numeroValido(numero):
    n = (len(numero) >= 3 and numero.isdigit()) or (numero[0]=="+" and len(numero) >= 4 and numero[1:].isdigit())
    return n



def registarChamada(origem, destino, duracao, chamadas):
    if numeroValido(origem) and numeroValido(destino) and duracao.isdigit():
        if origem in chamadas:
            chamadas[origem].append((destino, duracao))
        else:
            chamadas[origem] = [(destino, duracao)]
        return True
    








def Menu(m):
    MENU = "\n 1) Registar Chamada \n 2) Ler ficheiro \n 3) Ler clientes \n 4) Fatura \n 5) Terminar \n Opção?"
    chamadas = {}
    repetir = True
    while repetir:
        m = int(input(MENU))
        if m == "5":
            repetir = False
        elif m == "1":
            registarChamada(chamadas)
        elif m == "2":
            lerFicheiro()
        elif m == "3":
            clientes = sorted(chamadas.keys())
            print (clientes)
        elif m == "4":
            fatura()
        else:
            print("Opção inválida")
        
        

            
            
            
    
