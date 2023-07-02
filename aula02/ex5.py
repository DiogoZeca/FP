l = int(input("Litros de Combustível: "))

if l > 40:
    preco = (l * 1.4) - (l * 1.4) * 1/10
else:
    preco = l * 1.4


print("O preçco a pagar é de ", preco, "euros! ")
