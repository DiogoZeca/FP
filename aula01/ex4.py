def tempo():
    time = int(input("Introduza o tempo em segundos: "))

    horas = time // 3600
    minutos = (time % 3600) // 60
    segundos = minutos % 60

    print("{:02d} horas, {:02d} minutos e {:02d} segundos".format (horas, minutos, segundos))

tempo()