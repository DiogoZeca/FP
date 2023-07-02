x1 = float(input("number? "))
x2 = float(input("number? "))
x3 = float(input("number? "))


if x1 > x2 and x1 > x3:
    mx = x1
elif x2 > x1 and x2 > x3:
    mx = x2
else:
    mx = x3


print("Maximum:", mx)


#3, 2, 1