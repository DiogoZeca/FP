# Pode correr o programa sem argumentos:
#   python3 shop
# ou passando outros ficheiros de produtos como argumento:
#   python3 shop produtos1.txt ...

def loadDataBase(fname, produtos):
    # Ler dados do ficheiro fname
    with open(fname, "r") as file:
        for line in file.readlines()[1:]:
            # Lista com os dados de cada produto
            data = line.rstrip().split(";")
            # Atualizar dicionário com produtos no formato pedido {código: (nome, secção, preço, iva), ...}
            produtos[data[0]] = (data[1], data[2], float(data[3]), int(data[4][:-1])/100)


def registaCompra(produtos):
    """Regista a compra"""
    # Dicionário a ser devolvido pela função
    compra = {}
    text_input = input("Code? ")
    # Registar compras repetidamente até text_input ser uma linha vazia
    while text_input != '':
        # text_input deve ser do tipo "pX" ou "pX Y", sendo X um número entre 1 e o número de produtos e Y uma quantidade inteira positiva
        try:
            # Ler código (ou código e quantidade) do produto, separar por espaços, e guardar o primeiro elemento (referente ao código do produto)
            code = text_input.split()[0]
            if code in produtos.keys():  #text_input[0] == "p" and int(code[1:]) in list(range(1, len(produtos) + 1)):
                # Quantidade pré-definida
                quant = 1
                # A variável produto contém os dados do produto num tuple
                produto = produtos[code]
                # No caso do input ser do tipo "pX Y", e como quant tem de ser um número natural, se não fôr, gera um erro (programa avança para linha 42)
                if len(text_input.split()) != 1:
                    quant = int(text_input.split()[1])
                # Se o código do produto já existe no dicionário, soma a quantidade, senão é adicionado com o valor da quantidade
                if code in compra:
                    compra[code] += quant
                else:
                    compra[code] = quant
                # Mostrar nome, quantidade e preço final com duas casas decimais de cada produto
                print(produto[0], quant, round(quant*produto[2]*(1 + produto[3]), 2))
        except Exception:
            # Caso uma das condições em cima gere um erro, então o utilizador introduziu um valor inválido e deve introduzir um novo valor
            pass
        finally:
            # Este código é executado no fim do while loop e que serve para gravar o input na variável text_input no final de cada iteração
            text_input = input("Code? ")

    # Devolver dicionário com o formato pedido {codigo: quantidade, ...}
    return compra


def fatura(produtos, compra):
    """Imprime a fatura de uma dada compra."""
    # Variáveis de somatórios ao longo das iterações
    bruto, iva, liq, = 0, 0, 0
    # Dicionário que vai conter as secções como chaves e o resto dos dados das compras como valores
    compra_seccao = {}
    # Atualizar lista com dados dos produtos da compra e calcular o total bruto, total iva e total líquido
    for code in compra:
        # A variável produto contém dados do produto num tuple
        produto = produtos[code]
        # Quantidade obtida em registaCompra() por produto
        quant = compra[code]
        # Adiciona a secção à chave (se ainda não existir) e como valor, um tuple com: quantidade, nome, taxa em percentagem, preço líquido * quantidade
        if produto[1] not in compra_seccao:
            compra_seccao[produto[1]] = [(quant, produto[0], str(int(produto[3] * 100)) + "%", quant*produto[2]*(1 + produto[3]))]
        else:
            compra_seccao[produto[1]].append((quant, produto[0], str(int(produto[3] * 100)) + "%", quant*produto[2]*(1 + produto[3])))           
    
        # Somatórios
        bruto += produto[2] * quant
        iva += produto[3] * produto[2] * quant
        liq += produto[2] * (1 + produto[3]) * quant
    
    temp = ''
    # Imprimir cada produto por secção (chave do dicionário)
    for seccao in compra_seccao:
        # Verificar se secção já foi imprimida previamente nas iterações
        if seccao != temp:
            print(seccao)
        # Imprimir os dados de cada produto pedidos na formatação pedida
        for line in compra_seccao[seccao]:
            print("{:>4} {:<30} ({:>3}) {:>10.2f}".format(line[0], line[1], line[2], line[3]))
        # A variável temp fica com o valor da secção atual
        temp = seccao

    # Imprimir o total bruto, o total iva e o total líquido na formatação pedida
    print("{:>41} {:>10.2f}".format('Total Bruto:', bruto))
    print("{:>41} {:>10.2f}".format('Total IVA:', iva))
    print("{:>41} {:>10.2f}".format('Total Liquido:', liq))
        

def main(args):
    # produtos guarda a informação da base de dados numa forma conveniente.
    produtos = {'p1': ('Ketchup.', 'Mercearia Salgado', 1.59, 0.23)}
    # Carregar base de dados principal
    loadDataBase("produtos.txt", produtos)
    # Juntar bases de dados opcionais (Não altere)
    for arg in args:
        loadDataBase(arg, produtos)

    # Lista das diferentes compras
    compras = []
    # Use este código para mostrar o menu e ler a opção repetidamente
    MENU = "(C)ompra (F)atura (S)air ? "
    repetir = True
    while repetir:
        # Utilizador introduz a opção com uma letra minúscula ou maiúscula
        op = input(MENU).upper()
        # Processar opção
        if op == "C":
            # Esta opção regista os produtos de uma compra e adiciona à lista de compras
            compras.append(registaCompra(produtos))
        elif op == "F":
            # Utilizador introduz um número natural menor ou igual ao número de compras separadas
            esc = input("Numero compra? ")
            while not (esc.isdigit() and 0 < int(esc) <= len(compras)):
                print("Número inválido. Escreva um número inteiro positivo")
                esc = input("Numero compra? ")
            # Esta opção imprime a fatura da compra escolhida em cima
            fatura(produtos, compras[int(esc)-1])
        elif op == "S":
            # Esta opção termina o while loop
            repetir = False
        else:
            print("Input inválido.")

    print("Obrigado!")


# Não altere este código / Do not change this code
import sys
if __name__ == "__main__":
    main(sys.argv[1:])
