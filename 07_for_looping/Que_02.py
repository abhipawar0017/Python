#Nested for loop:--
# Write a program to check whether the entered number is prime or not in between a range:-

start = int(input("Enter start :"))
end =int(input("Enter the end :"))

for n in range(start,end+1):
  if n>1:
    for i in range(2,n):
      if (n% i==0):
        break
    else:
      print(n)
