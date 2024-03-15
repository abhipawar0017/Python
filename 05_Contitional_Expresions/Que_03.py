# Program to find the area of triangle and perimeter of triangle

n = input("Find ? 1 for area and 2 for perimeter :")
if(n=="1"):
  h =int(input("Enter the height :"))
  b =int(input("Enter the base :"))
  A = (h*b)/2
  print("Area : ",A)
elif(n=="2"):
  x =int(input("Enter the 1st side :"))
  y =int(input("Enter the 2nd side :"))
  z =int(input("Enter the 3rd side :"))
  P=x+y+z
  print("Perimeter :",P)
else:
  print("please select only between 1 & 2")
