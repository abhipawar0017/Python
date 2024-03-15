# Program which prints the fibonacci series of a number and write the conditions that nos should not be negative

n =int(input("Numbers want to print: "))

if(n>0):
  a=0
  b=1
  c=2
  print(a)
  print(b)
  while(c<=n):
    z=a+b
    print(z)
    a=b
    b=z
    c=c+1
else:
  print("Enter the positive number")
