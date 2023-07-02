#ID: 

# Complete...

# Use esta instrução / Use this instruction:

def taxaDeducao(rendimento):
   if rendimento > 20000:
      return [15, 1500]
   elif rendimento < 10000:
      return [5, 0]
   else:
      return [10, 500]

while True:
   info = input("Rendimento? ")    # Income?
   if not info:
      break
   
   rendimento = float(info)
   taxa, deducao = taxaDeducao(rendimento)
   
   imposto = ((taxa / 100) * rendimento) - deducao
   
   print("Imposto: {:.2f}".format(imposto))