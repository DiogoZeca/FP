from cmath import pi
import math

# You throw a dart that hits coordinates (x, y) on a dartboard.
# Create a program that gives you the score.
# See:
#   https://en.wikipedia.org/wiki/Darts#Dartboard
#   https://www.dimensions.com/element/dartboard

print("Enter the coordinates in mm from the center of the board.")
x = float(input("x? "))
y = float(input("y? "))

dist = math.sqrt(((x-0)**2)+((y-0)**2))
ang = math.degrees(math.atan2(y, x))

if ang < 0:
    ang += 360


if ang < 9:
    score = 6
elif ang < 27:
    score = 13
elif ang < 45:
    score = 4
elif ang < 63:
    score = 18
elif ang < 81:
    score = 1
elif ang < 99:
    score = 20
elif ang < 117:
    score = 5
elif ang < 135:
    score = 12
elif ang < 153:
    score = 9
elif ang < 171:
    score = 14
elif ang < 189:
    score = 11
elif ang < 207:
    score = 8
elif ang < 225:
    score = 16
elif ang < 243:
    score = 7
elif ang < 261:
    score = 19
elif ang < 279:
    score = 3
elif ang < 297:
    score = 17
elif ang < 315:
    score = 2
elif ang < 333:
    score = 15
elif ang < 351:
    score = 10
else:
    score = 6


if dist <= 0.4:
    scoref = 50
elif dist <= 1.2:
    scoref = 25
elif dist <= 9.9:
    scoref = score
elif dist <= 10.7:
    scoref = 3 * score
elif dist <= 16.2:
    scoref = score
elif dist <= 17:
    scoref = 2*score
else:
    scoref = 0

print("A sua pontuação foi de:",scoref)