
import math;

def triangulo():
    A = int(input("Indique o valor do cateto A: "))
    B = int(input("Indique o valor do cateto B: "))

    C = int(math.sqrt(A**2 + B **2))
    
    if(A > B):
        ang = float(math.acos(A/C))
    else:
        ang = float(math.acos(B/C))

    print("A Hipotenusa mede", C, "e tem um ângulo com {0:.2f} graus.".format(ang))

triangulo()

