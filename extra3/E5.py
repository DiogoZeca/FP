def printStocks(stocks):
#A+(A x V) = F
#V = F-A/A
   for stock in stocks:
      empresa, cidade, abertura, fecho, volume = stock
      valorizacao = (fecho - abertura) / abertura
      print("{:9s} {:15s} {:>9.2f} {:>9.2f} {:>9d} {:>6.1f}%".format(empresa, cidade, abertura, fecho, volume, valorizacao*100))
    