year=int("input year to be checked")
if (year%400==0):
  print("%d is a leap year"%year)
  elif(year%100==0):
    print("%d is NOT a leap year"%year)
    elif(year%4==0):
      print("%d is a leap year"%year)
else:
print("%d is nota leap year"%year)
