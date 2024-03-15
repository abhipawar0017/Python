# Program to generate student Result . Accept marks of five subject and display the result according to following conditions:-

# Percentage     Division
# >=75             First Class with Distinction
# >=60 and <75     First Class
# >=45 and <60     Second Class
# >=40 and <45     Pass
# <40              FAIL

res = float(input("Enter the result :"))
if(res>=75 and res<=100):
  print("First class with distinction")
elif(res>=60 and res<75):
  print("first class")
elif(res>=45 and res<60):
  print("Second class")
elif(res>=40 and res<45):
  print("pass")
elif(res<40 and res>=0):
  print("FAIL !!")
else:
  print("Result should be 0 to 100 !")
