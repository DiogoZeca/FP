# This program reads the coordinates of two points (x1,y1) and (x2,y2).
import math;
x1 = float(input("x1? "))
y1 = float(input("y1? "))
x2 = float(input("x2? "))
y2 = float(input("y2? "))

# Find and print the distance between the points!
# ...
dist=math.sqrt((x1-x2)**2 + (y1-y2)**2)

print(dist)
