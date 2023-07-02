   for vag in t[::-1]:
      if vag[M] != m:
         continue
      if vag[Q] > q:
         vag[Q] -= q
         q = 0
      else:
         q -= vag[Q]
         t.remove(vag)
   return q
      