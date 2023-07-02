from tkinter import filedialog

def main():
    # 1) Pedir nome do ficheiro (experimente cada alternativa):
    #name = input("File? ")                                  #A
    name = filedialog.askopenfilename(title="Choose File")   #B
    
    # 2) Calcular soma dos números no ficheiro:
    total = fileSum(name)
    
    # 3) Mostrar a soma:
    print("Sum:", total)


def isnumber(Value):
    try:
        float(Value)
    except ValueError:
        return False
    return True

def fileSum(filename):
    # Complete a função para ler números do ficheiro e devolver a sua soma.
    with open(filename, "r") as f:
        total = 0
        for line in f:
            if isnumber(line):
                total += float(line)
        return total

if __name__ == "__main__":
    main()

