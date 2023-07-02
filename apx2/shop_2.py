
def loadDataBase(fname, produtos):
    """Lê dados do ficheiro fname e atualiza/acrescenta a informação num
    dicionário de produtos com o formato {código: (nome, secção, preço, iva), ...}.
    """
    with open(fname, 'r') as fileobj:
        lines = fileobj.readlines()[1:]
        for line in lines:
           words = line.split(';')
           code = words[0]
           produtos[code] = (words[1], words[2], words[3], words[4].replace('\n', ''))

def registaCompra(produtos):
    """Lê códigos de produtos (ou códigos e quantidades),
    mostra nome, quantidade e preço final de cada um,
    e devolve dicionário com {codigo: quantidade, ...}
    """
    compras = dict()
    while True:
       registo = input('Code? ')
       registo = registo.split(" ")
       code = registo[0]
       if len(registo) > 1:
          quantidade = int(registo[1])
       else:
          quantidade = 1
       if code in produtos.keys():
          nomeProduto = produtos[code][0]
          preçoFinal = round(quantidade * (float(produtos[code][2]) * (1 + float(produtos[code][3].strip('%')) / 100)), 2)
          print(nomeProduto, quantidade, preçoFinal)
       if code == "":
          break
       if code in produtos.keys():
          if code not in compras.keys():
             compras[code] = quantidade
          else:
             compras[code] += quantidade
    return compras

def fatura(numeroCompra, produtos):
    """Imprime a fatura de uma dada compra."""
    current_merc = ''
    brutoTotal = 0
    IVATotal = 0
    for code in numeroCompra.keys():
       mercearia = produtos[code][1]
       if current_merc != mercearia:
          current_merc = mercearia
          print(mercearia)
       quantidade = numeroCompra[code]
       produto = produtos[code][0]
       IVA = produtos[code][3]
       PreçoComIVA = quantidade * (round(float(produtos[code][2]) * (1 + float(produtos[code][3].strip('%')) / 100), 2))
       print("{0:>4d} {1:30s} ({2:>3s}) {3:11.2f}".format(quantidade, produto, IVA, PreçoComIVA))
       brutoTotal += quantidade * float(produtos[code][2])
       IVATotal += quantidade * (round(float(produtos[code][2]) * (float(produtos[code][3].strip('%')) / 100), 2))
    print("{0:>41s} {1:11.2f}".format('Total Bruto:', round(brutoTotal, 2)))
    print("{0:>41s} {1:11.2f}".format('Total IVA:', round(IVATotal, 2)))
    liquidoTotal = brutoTotal + IVATotal
    print("{0:>41s} {1:11.2f}".format('Total Liquido:', round(liquidoTotal, 2)))

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
    numeroCompra = dict()
    key = 1
    repetir = True
    while repetir:
       op = input(MENU).upper()
       if op == 'C':
          compra = registaCompra(produtos)
          numeroCompra[key] = compra
          key += 1
       elif op == 'F':
          num = int(input('Numero compra? '))
          nCompra = numeroCompra[num]
          imprimirFatura = fatura(nCompra, produtos)
       elif op == 'S':
          print("Obrigado!")
          break

# Não altere este código / Do not change this code
import sys
if __name__ == "__main__":
    main(sys.argv[1:])