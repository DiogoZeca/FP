# Complete o programa!

# a)
def loadFile(fname, lst):
     with open(fname) as f:
        for line in f:
            line = line.strip('\n')
            if not line[0].isnumeric(): continue
            lineSplit = line.split('\t')
            tupleToAdd = (int(lineSplit[0]), lineSplit[1], float(lineSplit[5]), float(lineSplit[6]), float(lineSplit[7]))
            lst.append(tupleToAdd)
    
# b) Crie a função notaFinal aqui...
def notaFinal(reg):
    nota1, nota2, nota3 = reg[2], reg[3], reg[4]
    notaFinal = ( nota1 + nota2 + nota3 ) / 3
    return notaFinal

# c) Crie a função printPauta aqui...
def printPauta(lst):
    print('{:>10} {:^50} {:>8.1}'.format("Nùmero", "Nome", "Nota"))
    for reg in lst:
        print('{:>10} {:^50} {:>8.1f}'.format(reg[0], reg[1], notaFinal(reg)))



def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    lst.sort()
    
    # mostrar a pauta
    printPauta(lst)


# Call main function
if __name__ == "__main__":
    main()