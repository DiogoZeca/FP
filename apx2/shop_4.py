def loadDataBase(fname, produtos):
    try:
        file = open(f"{fname}", "r", encoding='utf-8')          
    except OSError:
        print("Error opening file")
        return
    lines = file.readlines()
    for line in lines:
        lst = line.split(";")
        if(lst[0] == "CODIGO"):
            pass
        else:
            codigo = lst[0]
            nome = lst[1]
            seccao = lst[2]
            preço_base = float(lst[3])
            taxa = int(lst[4][:-2])
            produtos[codigo] = (nome, seccao, preço_base, taxa)

    file.close()           

def registaCompra(produtos):
    carrinho = {}          # Cria-se um dicionário para registar cada produto que se pede num só sítio
    n = "1"
    while n != "":
        n = input("Code? ")
        x = n.split()          # Faz-se uso da função ".split()" para se puder dar o valor da quantidade que se quer comprar de um certo produto, ou seja, o "CODIGO" não é a única coisa permita
        if(len(x) > 1):          # Caso em que é introduzido uma quantidade para o produto
           if x[0] in produtos:
               b = float(produtos[x[0]][-2]) * ((float(produtos[x[0]][-1])/ 100) + 1) * float(x[1]) # Preço final
               print("{} {} {:.2f}".format(produtos[x[0]][0],x[1],b))
               if not x[0] in carrinho:
                   carrinho.update({x[0] : x[1]})         # x[0] corresponde ao "CODIGO" e x[1] corresponde à quantidade
               else:
                   carrinho[x[0]] += int(x[1])
        elif(len(x) == 1):       # Caso em que é introduzido apenas o "CODIGO" do produto
           if n in produtos:
               b = float(produtos[n][2]) + (float(produtos[n][3]) / 100) * float(produtos[n][2])
               print("{} {} {:.2f}".format(produtos[n][0],"1",b))
               if not n in carrinho:
                   carrinho.update({n :1})
               else:
                   carrinho[n] += 1
        else:
           pass     # Situações em que são introduzidos valores inválido ex: -5; ceb; ...
    return carrinho
def fatura(produtos, compra):
    b = i = l = 0         # A variável "b" corresponde ao total bruto, a variável "i" corresponde ao total iva, a variável "l" corresponde ao total líquido
    categoria = []        # Cria-se uma lista para armazenar cada registo de compra

    for q in compra:
        if q in categoria:
            continue
        print (produtos[q][1])
        for t in compra:
            if produtos[t][1] == produtos [q][1]:

                p = float(produtos[t][-2]) * ((float(produtos[t][-1])/ 100) + 1) * float(compra[t])       # Preço Final
                l = l + p
                b = b + float(produtos[t][-2]) * float(compra[t])
                i = i + float(produtos[t][-2]) * (float(produtos[t][-1]) / 100) * float(compra[t])
                print("{:<3} {:>20} ({:2d}%) {:>10.2f}".format(compra[t],produtos[t][0],produtos[t][3],p))
                categoria.append(t)
    print("{:>55} {:>10.2f}".format("Total Bruto:",b))
    print("{:>55} {:>10.2f}".format("Total Iva:",i))
    print("{:>55} {:>10.2f}".format("Total Liquido:",l))
def main(args):
    # produtos guarda a informação da base de dados numa forma conveniente.

    produtos = {'p1': ('Ketchup.', 'Mercearia Salgado', 1.59, 0.23)}

    # Carregar base de dados principal

    loadDataBase("produtos.txt", produtos)

    # Juntar bases de dados opcionais (Não altere)

    for arg in args:
        loadDataBase(arg, produtos)

    # Use este código para mostrar o menu e ler a opção repetidamente

    MENU = "(C)ompra (F)atura (S)air ? "

    c = []

    while True:

        # Utilizador introduz a opção com uma letra minúscula ou maiúscula

        op = input(MENU).upper()

        # Processar opção
        
        if op == "C":
            c.append(registaCompra(produtos))
        elif op == "F":
            n = int(input("Numero compra? "))
            fatura(produtos, c[n - 1])
        elif op == "S":
            break
    print("Obrigado!")


# Não altere este código / Do not change this code
import sys
if __name__ == "__main__":
    main(sys.argv[1:])
