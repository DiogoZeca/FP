CTP = int(input("Introduz nota da componente Teorico-Pratica: "))
CP  = int(input("Introduz nota da componente Prática: "))

if CP and CTP < 6.5:
    print(" 66 ")

nota = (0.7 * CP) + (0.3 * CTP)

if nota > 20:
    print("Dados errados!")
elif 6.5 < nota < 10:
    print("Inserir notas dos testes de Recurso!")

    ATPR = int(input("Introduz nota da componente Teorico-Pratica: "))
    APR  = int(input("Introduz nota da componente Prática: "))
    notaR = (0.7 * ATPR) + (0.3 * APR)
    if notaR > 9.5:
        print("Nota Final de Recurso: {:.02f}".format(notaR))
    else:
        print("Reprovado!")

else:
    print("Nota Final: {:.02f}".format(nota))

