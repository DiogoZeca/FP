# Pode correr o programa sem argumentos:
#   python3 shop
# ou passando outros ficheiros de produtos como argumento:
#   python3 shop produtos1.txt ...

import sys



def loadDataBase(fname, produtos):
    """Lê dados do ficheiro fname e atualiza/acrescenta a informação num
    dicionário de produtos com o formato {código: (nome, secção, preço, iva), ...}.
    """
    with open(fname, "r") as f:
        next(f)
        for i in f:
            i = i.split(";")
            # replace para tirar o \n e o %
            produtos[i[0]] = (i[1], i[2], float(i[3]), float(i[4].replace("%", "").replace("\n", ""))/100)


def registaCompra(produtos):
    """Lê códigos de produtos (ou códigos e quantidades),
    mostra nome, quantidade e preço final de cada um,
    e devolve dicionário com {codigo: quantidade, ...}
    """
    quantidades = {}
    while True:
        codigo = input("Code? ")
        if codigo == "":
            break
        split = codigo.strip().split(" ")
        if split[0] in produtos:
            if len(split) == 1:
                codigo = split[0]
                quantidades[codigo] = quantidades.get(codigo, 0) + 1
                valor = 1
            else:
                codigo = split[0]
                try:
                    quantidades[codigo] = quantidades.get(codigo, 0) + int(split[-1])
                    valor = int(split[-1])
                except ValueError:
                    quantidades[codigo] = quantidades.get(codigo, 0) + 1
                    valor = 1
            print("{} {} {:.2f}".format(produtos[codigo][0], valor, valor *produtos[codigo][2] + valor * (produtos[codigo][2]*produtos[codigo][3])))
        else:
             continue
    #print(quantidades)
    return quantidades


def fatura(produtos, compra):
    """Imprime a fatura de uma dada compra."""
    Bruto = 0
    IVA = 0
    liquido = 0
    IVA_Total = 0
    categoria = {}
    for prod in compra:
        cat = produtos[prod][1]
        if cat in categoria:
            categoria[cat].append(prod)
        else:
            categoria[cat] = [prod]
    for category in categoria:
        print(category)
        prods = categoria[category]
        for produto in prods:  # {p2:2}
            Qnt = compra[produto]
            nome = produtos[produto][0]
            IVA = produtos[produto][3]
            preco = produtos[produto][2] + (produtos[produto][2]*IVA)
            total = Qnt * preco

            liquido += total
            IVA_Total += Qnt*IVA*produtos[produto][2]
            Bruto = liquido - IVA_Total

            print("{:>4} {:<30} ({:>2}%) {:>10.2f}".format(Qnt, nome, int(IVA*100), total))
    print("{:>41} {:>10.2f}".format("Total Bruto:", Bruto))
    print("{:>41} {:>10.2f}".format("Total IVA:", IVA_Total))
    print("{:>41} {:>10.2f}".format("Total Liquido:", liquido))


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
    repetir = True
    faturas = []
    while repetir:
        # Utilizador introduz a opção com uma letra minúscula ou maiúscula
        op = input(MENU).upper()
        # Processar opção
        if op == "C":
            # Esta opção regista os produtos de uma compra
            compra = registaCompra(produtos)
            # Aqui pode acrescentar a compra a uma estrutura de dados adequada...
            faturas.append(compra)
        elif op == "S":
            # Esta opção termina o programa
            repetir = False
        elif op == "F":
            num_compra = input("Numero compra? ")
            try:
                num_compra = int(num_compra)
            except ValueError:
                num_compra = 1
            if (len(faturas) < num_compra) or (num_compra < 1):
                print("Compra não existe")
            else:
                fatura(produtos, faturas[num_compra-1])
            # Esta opção imprime a fatura de uma compra


    print("Obrigado!")


# Não altere este código / Do not change this code
if __name__ == "__main__":
    main(sys.argv[1:])
