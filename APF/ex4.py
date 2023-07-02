def portfolioValue(stocks, C):
   money = 0
   
   for action, amount in C.items():
      money += stocks[action] * amount
      
   return money