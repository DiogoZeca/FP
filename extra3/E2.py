# Given a sequence lst, return the longest n so that 
# the first n elements equal the last n elements (with no overlapping).

# Dada uma sequência lst, devolva o maior n tal que
# os primeiros n elementos igualam os últimos n elementos (sem sobreposição).

def firstEqualLast(lst):
    count = 0
    l = len(lst) // 2 + 1
    for i in range(l):
       if lst[:i] == lst[-i:]:
          count = i
    return count
   