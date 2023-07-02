# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle


t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here
text = open("/Users/diogo/Documents/CT 2.1/FP/aula06/drawing.txt" , "r")
b = []
for line in text:
    line = line.strip()
    if line == "UP":
        t.up()
    elif line == "DOWN":
        t.down()
    else:
        b = line.split()
        x = b[0]
        y = b[1]
        t.goto(int(x), int(y))

# wait
turtle.Screen().exitonclick()

