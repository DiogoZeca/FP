def tax(r):
    if r <= 1000:
        return 0.1*r
    elif r <= 2000:
        return 0.2*r - 100
    elif r > 2000:
        return 0.3*r - 300

valor = float(input("Qual é o rendimento? "))

print("A taxa de rendimento é de:", tax(valor),"€")