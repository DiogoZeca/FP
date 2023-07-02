lst = [1, 2, 3, 4, 5]

def inList(num, lst):
    for i in lst:
        if i == num:
            return True
    return False

def main():
    num = int(input("Digite um número: "))
    if inList(num, lst):
        print("O número está na lista")
    else:
        print("O número não está na lista")
main()