# Nested Loops :--
# 1
# 1 2
# 1 2 3
# 1 2 3 4

n= int(input("How many lines you want to priont :"))
i=1
while(i<=n):
  j=1
  while(j<(i+1)):
    print(j, end = ' ')
    j=j+1
  i=i+1
  print()
