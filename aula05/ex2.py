def inputFloatList():
    lst = []
    while True:
        num = input("Introduza um número: ")
        if num == "":
            break
        elif not num.isnumeric():
            print("Isso não é um número animal")
        else:
            lst.append(int(num))
    return lst

def countLower(lst, v):
    i = 0
    for num in lst:
        if num < v:
            i += 1
    return i

def minmax(lst):
    max = lst[0]
    min = lst[0]
    for i in lst:
        if i > max:
            max = i
        if i < min:
            min = i
    return max, min

def medio(lst, max, min):
    valor = (max + min) / 2
    inferior = 0
    for i in lst:
        if i < valor:
            inferior += 1
    return valor, inferior

def main():
    lst = inputFloatList()
    max, min = minmax(lst)
    valor, inferior = medio(lst, max, min)
    
    print("Lista: ", lst)
    print("Valor máximo é: ", max)
    print("Valor mínimo é: ", min)
    print("Valor médio é: ", valor)
    print("Tem",inferior,"valores inferiores ao valor médio.")

main()
    


            




        