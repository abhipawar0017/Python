# Program to print the following pattern

# *
# * *
# * * *
# * * * *

i=1
while(i<5):
  j=1
  while(j<(i+1)):
    print('*', end=' ')
    j=j+1
  i=i+1
  print()
