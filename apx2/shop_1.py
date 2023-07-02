# Constantes para facilitar a leitura do código
MENU, NAME, SECTION, PRICE, IVA = "(C)ompra (F)atura (S)air ? ", 0, 1, 2, 3


def load_data_base(file_name, products):
    """Esta função adiciona ou atualiza os produtos de uma base de dados"""

    with open(file_name, "r", encoding="utf8") as file:
        # Lê cada linha do ficheiro e separa os campos usand ";" como separador
        # Adicionalmente faço um slice para não incluir a primeira linha que é irrelevante
        split_data = tuple(line.strip().split(";") for line in file)[1:]

    # Não se assustem se não entenderem pesquisem e não me desçam a nota
    # Eu mapeio a função lambda abaixo para cada elemento da lista anterior
    # O objetivo é converter o preço em float e a percentagem em float decimal
    # O replace("%", "e-2") é para converter 99.5% em 99.5e-2 (99.5*10^(-2)) que quando convertido para float dá 0.995
    split_data_converted = map(lambda x: (*x[:3], float(x[3]), float(x[4].replace("%", "e-2"))), split_data)

    # Por fim adiciono cada produto à base de dados
    for data in split_data_converted:
        products[data[0]] = data[1:]

    # Este return é desnecessário, contudo poderá ser útil no futuro
    return products


def register_purchase(products):
    """Esta função regista uma compra que irá ser usada no futuro para gerar uma fatura.
    Ela guarda o id do produto e a quantidade comprada"""

    # Cria um dicionário vazio para guardar os produtos da compra
    purchase_data = dict()

    # O utilizador insere o id do produto e a quantidade
    # Sendo assim usa-se o strip para limpar o texto e o split para separar o id da quantidade
    user_input = input("Code? ").strip().split()

    # Objetos vazios (0, 0.0, [], {}, "", None, etc) quando covertidos para boolean devolvem False
    # Assim enquanto o utilizador inserir informação não vazia o ciclo continua
    while user_input:
        # Se o utilizador apenas inserir um id sem quantidade, a quantidade por defeito é 1
        if len(user_input) == 1:
            user_input.append("1")  # O "1" é uma string porque no if que vem asseguir tenho de passa-lo como string

        # Esta condição verifica se o id do produto existe na base de dados, caso contrário ignora
        # Também verifica se o tamanho da lista criada por user_input é 2
        # Por fim, verifica se a quantidade inserida é efetivamente um número inteiro positivo (pesquisar .isnumeric())
        if user_input[0] in products and len(user_input) == 2 and user_input[1].isnumeric() and user_input[1] != "0":
            # Neste passo por questões de organização separei a quantidade e o id em duas variáveis
            product_id, quantity = user_input[0], int(user_input[1])

            # Se o produto já existir na compra, adiciona a quantidade caso contrário adiciona o produto e a quantidade
            purchase_data[product_id] = purchase_data.get(product_id, 0) + int(quantity)

            # Calcula o preço final do produto
            product_price = products[product_id][PRICE] * (1 + products[product_id][IVA]) * quantity

            # Imprime o nome do produto, a quantidade e o preço final
            print(f"{products[product_id][NAME]} {quantity} {product_price:.2f}")

        user_input = input("Code? ").strip().split()
    return purchase_data


def invoice(products, purchase):
    """Esta função imprime a fatura de uma compra e calcula o preço final"""

    # Dicionário vazio que será usado para organizar os produtos por secção
    organized_purchase = dict()

    # Este ciclo percorre todos os produtos da compra e as respetivas quantidades para organizar a informação
    # de uma maneira mais fácil de processar, agrupando os produtos por secção.
    for product, quantity in purchase.items():
        # Por questões de organização criei uma variável para a secção onde o produto será adicionado
        section = products[product][SECTION]

        # Este tuplo irá ser usado para organizar os produtos pela ordem que vão ser representados no final
        organize_section = (quantity, products[product][NAME], products[product][IVA], products[product][PRICE])

        # Se a secção já existir no dicionário, adiciona o produto caso contrário cria a secção e adiciona o produto
        organized_purchase[section] = organized_purchase.get(section, []) + [organize_section]

    # Este ciclo percorre todas as secções e os seus produtos
    for section, product in organized_purchase.items():
        print(section)
        for item in product:
            # Cria uma variável para cada elemento da lista para organizar melhor o código
            quantity, name, iva, price = item
            # Calcula o preço final do produto
            final_price = price * (1 + iva) * quantity
            # Hmmmm... yah em poucas palavras isto formata a string para ficar como é pretendido
            print(f"   {f'{quantity} {name}':33}({iva:>3.0%}){final_price:>11.2f}")

    # Cálculo das 3 categorias de preço que vão ser mostrados no final
    # As compreesões calulam o preço de cada produto presentes na compra e cria um gerador(uma lista mais eficiente)
    # com todos os preços e depois usa-se a função sum para somar todos os preços gerados
    brute_price = sum(products[p][PRICE] * q for p, q in purchase.items())
    tax_price = sum(products[p][PRICE] * products[p][IVA] * q for p, q in purchase.items())
    final_price = brute_price + tax_price
    # Formatação da representação final dos preços
    # Fiz um tuplo para não estar a repetir o código
    print_tuple = (("Total Bruto:", brute_price), ("Total IVA:", tax_price), ("Total Liquido:", final_price))
    for item in print_tuple:
        # Formata os preços guardados no tuplo para ficarem como é pretendido
        print("{:>41}{:>11.2f}".format(*item))


def main(args):
    # Este contador é usado para listar as compras
    counter = 1
    # Dicionário vazio que será usado para guardar as compras
    purchase_dict = dict()

    products = {'p1': ('Ketchup.', 'Mercearia Salgado', 1.59, 0.23)}
    load_data_base("produtos.txt", products)
    # Juntar bases de dados opcionais (Não altere)
    for arg in args:
        load_data_base(arg, products)

    while True:
        op = input(MENU).upper()

        # Processar opção
        if op == "C":
            # Esta opção regista os produtos de uma compra
            purchase = register_purchase(products)

            # Se a compra não for vazia adiciona-a ao dicionário de compras
            if purchase:
                # A chave é o contador que é incrementado a cada compra válida
                purchase_dict[str(counter)] = purchase
                counter += 1

        elif op == "F":
            # Esta opção imprime a fatura de uma compra

            user_input = input("Numero compra? ").strip()

            # Verifica se oque foi inserido é válido caso contrário ignora
            if user_input in purchase_dict:
                # Por questões de organização criei uma variável
                purchase_info = purchase_dict[user_input]
                invoice(products, purchase_info)

        elif op == "S":
            # Esta opção termina o programa
            break

    print("Obrigado!")


# Não altere este código / Do not change this code
import sys

if __name__ == "__main__":
    main(sys.argv[1:])
