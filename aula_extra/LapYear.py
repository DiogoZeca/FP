def isLeapYear(year):
   if year%4 == 0 and year%100 != 0:
      return True
   elif year%400 == 0:
        return True
   else:
        return False
      
# monthDays deve devolver o número de dias de um dado mês num dado ano.
# Por exemplo, monthDays(2004, 2) deve devolver 29.
# Corrija-a.

def monthDays(year, month):
   if isLeapYear(year) == True:
         MONTHDAYS = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
   else:
      MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
      
   days = MONTHDAYS[month]
   return days


# nextDay deve devolver o dia a seguir a uma dada data.
# Por exemplo, nextDay(2017, 1, 31) deve devolver (2017, 2, 1)

def nextDay(year, month, day):
   
   if month in ([1,3,5,7,8,10]) and day == 31:
      month += 1
      day = 1
   elif isLeapYear(year) == True and month == 2 and day == 29:
        month = 3
        day = 1
   elif isLeapYear(year) == True and month == 2 and day == 28:
        day = 29
   elif month == 2 and day == 28:
        month = 3
        day = 1
   elif month == 12 and day == 31:
        year += 1
        month = 1
        day = 1
   else:
        day += 1
   return year, month, day


# Defina uma função dateIsValid que deve
# devolver True se os seus argumentos formarem uma data válida
# e devolver False no caso contrário.
# Por exemplo, dateIsValid(1980, 2, 29) deve devolver True,
# dateIsValid(1980, 2, 30) deve devolver False.
def dateIsValid(year, month, day):
   
   if month == any([1,3,5,7,8,10,12]) and (day > 31 or day < 1):
      return False
   elif month == any ([4,6,9,11]) and (day > 31 or day < 1):
       return False
   elif isLeapYear(year) == True and month == 2 and (day > 29 or day < 1):
       return False
   elif isLeapYear(year) == False and month == 2 and (day > 28 or day < 1):
        return False
   else:
      return True


# Defina uma função previousDay que devolva o dia anterior a uma dada data.
# Por exemplo, previousDay(1980, 3, 1) deve devolver (1980, 2, 29)
def previousDay (year, month, day):
   if month == any ([2,4,6,8,9,11]) and day == 1:
       month -= 1
       day = 31
   elif month == 1 and day == 1:
         year -= 1
         month = 12
         day = 31
   elif isLeapYear(year) == False and month == 3 and day == 1:
         month -= 1
         day = 28
   elif isLeapYear(year) == True and month == 3 and day == 1:
         month -= 1
         day = 29
   
   elif month == any([5,7,10,12]) and day == 1:
        month -= 1
        day = 30
   else:
        day -= 1
   return year, month, day

# No Codecheck, não chame nenhuma função: o sistema trata disso.