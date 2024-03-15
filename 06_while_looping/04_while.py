#Program to find the sum of the digits of given number

num = int(input("Enter a no : "))

s=0
while(num>0):
  rem = num%10
  s= s+rem
  num= int(num/10)
print("Addition : ",s)
