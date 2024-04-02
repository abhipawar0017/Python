#Program to check the nos is palindrome or not
n1 = int(input("Enter the num :"))
rev = 0
n2 = n1
while n2 >0:
  rem=n2 % 10
  rev= rev*10 + rem
  n2=int(n2/10)
if (n1==rev):
  print("Number is palindrome")
else:
  print("Number is not palindrome")
