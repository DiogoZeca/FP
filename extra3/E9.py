   dict = {}  
   for train in trains.keys():                    #cada comboio    "train" ---> T1 ou T2
      for vag in trains[train]:                   #cada vagao      "vag"   ---> ['iron', 53]
         mat = vag[M]                             #cada material   "mat"   ---> 'iron'
         if mat not in dict.keys():
            dict[mat] = {train}
         else:
            dict[mat].add(train)
   return dict               
   