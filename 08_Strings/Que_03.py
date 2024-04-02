#Program to check the string is palindrome or not:--
# Example if string is :-
# 1)nitin then its palindrome is nitin
# 2)abc then its palindrome is cba

a = input("Enter a string :")
b= a[-1: :-1]
print("1) Reverse of the string is  :",b)
if(a==b):
  print("2) String is palindrome")
else:
  print("2) String is not paindrome")
