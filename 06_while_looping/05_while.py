#Program to find out the reverse of  a given nos

n = int(input("Enter num : "))

r=0
while(n>0):
  rem =n%10
  r= r*10+rem
  n= int(n/10)
print("Reverse num :",r)
