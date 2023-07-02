def retangulo():
    largura = int(input("Digite a largura: "))
    altura = int(input("Digite a altura: "))

    area = largura * altura
    perimetro = 2 * (largura + altura)

    print("A área do retângulo é: ", area)
    print("O perímetro do retângulo é: ", perimetro)

retangulo()