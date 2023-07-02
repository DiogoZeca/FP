def countdown(N):
    if N == 0:
        print("Fogo!")
    else:
        print(N)
        countdown(N-1)

valor = int(input("Qual é o valor? "))
countdown(valor)
