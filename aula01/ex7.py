from tokenize import Double


def andares():
    #1 piso=== 12mx2 == 24m
    #2 piso=== 24mx2 == 48m
    #3 piso=== 36mx2 == 72m 
    #total == 24+48+72 = 144m = 0.144km

    percorrido = 144 * 365
    distancia = int(0.144 * 365)
    tempo = float(percorrido / 3600)

    print(distancia, "km em", tempo, "horas")

andares()