# Program to find the best of two test avearage marks out of three and  test's marks is accepted from the user

a = int(input("Enter the marks of 1st test :"))
b = int(input("Enter the marks of 2nd test :"))
c = int(input("Enter the marks of 3rd test :"))

if(a>b and a>c):
  print("The marks of the 1st test is highest")
elif(b>c and b>a):
  print("The marks of the 2nd test is highest")
else:
  print("The marks of the 3rd test is highest")
