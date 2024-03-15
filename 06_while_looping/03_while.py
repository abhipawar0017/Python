# Fibonacci Sequence

n = int(input("How many numbers want to print : "))
a = 0
b = 1
c = 2
print(a)
print(b)
while(c<=n):
  z=a+b
  print(z)
  a=b
  b=z
  c=c+1
