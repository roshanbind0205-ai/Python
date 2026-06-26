n=7

for i in range(n):
    for j in range(n):
         condition=j == i or j + i == n - 1
         if condition:
             print(" *",end="")
         else:
             print("  ",end="")
    print()