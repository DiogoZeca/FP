
# On a chessboard, positions are marked with letters between a and h for the column and a
# number between 1 and 8 for the row. The first place on the board, a1, is black. The next
# is white, alternating across a row. Odd rows start with black, even rows start with white.    #column[a..h]
# Give a 2 character input string with a letter (a-h) and a number (1-8), print "Black" or      #Row[1..8]
# "White" indicating if the square is black or white.                                           #A1 --- > Black

inputStr = 'a1' 
blck = ["a", "c", "e", "g"]
wht = ["b", "d", "f", "h"]
if int(inputStr[1]) % 2 == 0 and inputStr[0] in wht:
   print("Black")
elif int(inputStr[1]) % 2 !=0 and inputStr[0] in blck:
   print("Black")
else:
   print("White")
 