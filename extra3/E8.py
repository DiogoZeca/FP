   with open("stocks.txt", "r") as f:
      lst = []
      for line in f:
         lst.append(tuple(line.strip().split("\t")))
         for i, (empresa, cidade, abertura, fecho, volume) in enumerate(lst):
            lst[i] = (str(empresa), str(cidade), float(abertura), float(fecho), int(volume))
      return lst

