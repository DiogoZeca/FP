import math
def factorial(n):
    assert n > 0
    if n < 2 :
        return 1
    else:
        return n * factorial(n-1)

val = int(input("Valor para fatorizar: "))
print("O valor fatorizado é: ", factorial(val))


