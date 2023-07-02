
import math

def floatInput(prompt, min=None , max=None ):
  res = input(prompt)
  try:
    res = float(res)
    if min != None and res < min:
            print("ERROR: Value should be in [3, 0]!")
            return floatInput(prompt, min, max)
    if max != None and res > max:
            print("ERROR: Value should be in [3, 0]!")
            return floatInput(prompt, min, max)
    return res
  except ValueError:
    print("ERROR: Not a float!")
    return floatInput(prompt)


def main():
    print("a) Try entering invalid values such as 1/2 or 3,1416.")
    v = floatInput("Value? ")
    print("v:", v)

    print("b) Try entering invalid values such as 15%, 110 or -1.")
    h = floatInput("Humidity (%)? ", 0, 100)
    print("h:", h)

    print("c) Try entering invalid values such as 23C or -274.")
    t = floatInput("Temperature (Celsius)? ", min =-273.15)
    print("t:", t)

    # d) What happens if you uncomment this?
    impossible = floatInput("Value in [3, 0]? ", min=3, max=0)
    #nao funciona, devia ter o 3 e o 0 trocados

if __name__ == "__main__":
    main()
