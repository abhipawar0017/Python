# To Check if the input year is leap year and check if input year is leap year

y = int(input("Enter a leap year :"))
if (y%4 == 0 or  y%400 ==0):
  print(y , " is a leap year.")
else:
  print(y , "is not a leap year.")
