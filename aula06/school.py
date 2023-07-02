# Complete o programa!

# a)
def loadFile(fname, lst):
    # ler o ficheiro
    with open(fname) as f:
    # ler cada linha
        for line in f:
        # separar os campos
            line = line.strip('\n')
            if not line[0].isnumeric(): 
                continue            
        # criar um dicionário com os campos #0,1,5,6,7
            lineSplit = line.split('\t')      
            tupleToAdd = (int(lineSplit[0]), (lineSplit[1]), (float(lineSplit[5])), (float(lineSplit[6])), (float(lineSplit[7])))
            lst.append(tupleToAdd)
        return lst
    
# b) Crie a função notaFinal aqui...
def notaFinal(tuplo): #2,3,4
    nota2, nota3, nota4 = tuplo[2], tuplo[3], tuplo[4]
    notaFinal = (nota2 + nota3 + nota4) / 3
    return notaFinal
        
# c) Crie a função printPauta aqui...
def printPauta(lst):
    print('{:>10}, {:^50}, {:>8.1}'.format("Número", "Nome", "Nota"))
    for tuplo in lst:
        print('{:>10}, {:^50}, {:>8.1}'.format(tuplo[0], tuplo[1], notaFinal(tuplo)))


# d)
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


