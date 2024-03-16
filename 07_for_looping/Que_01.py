# Write a program to check whether the entered number is prime or not

n = int(input("Enter a number :"))
for i in range(2,(n+1)):
  if(n % i == 0):
    break
if(n==i):
  print("Number is prime")
elif(n==1):
  print("can't determine")
else:
  print("Entered number is not a prime")
