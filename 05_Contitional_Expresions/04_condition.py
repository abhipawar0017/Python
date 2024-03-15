# Program to check the largest number among the three numbers

x = int(input("Enter a  first number : "))
y = int(input("Enter a second number : "))
z = int(input("Enter a third number : "))

if(x>y and x>z):
  m = x
elif(y>z and y>x):
  m = y
else:
  m = z

print("Largest Number is",m)
