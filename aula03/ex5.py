def max1(x1, x2):
    bolota = x1
    if (x1 < x2):
        bolota = x2
    return bolota

def maior(xy, x3):
    boiola = xy
    if (xy < x3):
        boiola = x3
    return boiola

def main():
    x1 = int(input("Introduz um vaor para X1: "))
    x2 = int(input("Introduz um vaor para X2: "))
    x3 = int(input("Introduz um vaor para X3: "))
    xy = max1(x1, x2)

    print("O maior valor é: ", maior(xy, x3))
main()