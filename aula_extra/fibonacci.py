def genFibonacci(n):
   assert n >= 2
   lst=[0, 1]
   c = 0
   c1 = 1
   for i in range(2, n):
      lst.append(c + c1)
      c = lst[-1]
      c1 = lst[-2]
   return lst
print(genFibonacci(10))
   
#OU 


def genFibonacci2(n):
   assert n >= 2
   # Complete ...
   lst = []
   for i in range(n):
      if i == 0:
         lst.append(0)
      elif i == 1:
         lst.append(1)
      else:
         lst.append(lst[i-2] + lst[i-1])
   return lst
print(genFibonacci2(10))