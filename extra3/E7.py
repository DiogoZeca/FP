   lst = []
   for i in stocks:
      if city == i[1]:
         lst.append((i[0], i[4]))
   return lst