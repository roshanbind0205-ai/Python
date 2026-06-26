n = 7

for i in range(1, n + 1):

    # 1st letter
    for j in range(1, n + 1):
        condition = (
          (j==1)or(i==1 and j<=5)or(j==5 and i<=4) or(i==4 and j<=5)or(i-j==2) )
        
        if condition:
            print(" *",end="")
        else:
            print("  ",end="")
    print(" ",end="")
            
    for j in range(1, n + 1):
        condition = ((j == 1) or (j == 5) or(i == 1 and j <= 5) or(i == 7 and j <= 5) )
           
        if condition:
            print(" *", end="")
        else:
            print("  ", end="")

    print(" ", end="")

    for j in range(1, n + 1):
        condition = (
            (i == 1 and j <= 5) or(i == 4 and j <= 5) or(i == 7 and j <= 5) or(j == 1 and i <= n // 2) or(j == 5 and i > n // 2))

        if condition:
            print(" *", end="")
        else:
            print("  ", end="")

    print("", end="")

    for j in range(1, n + 1):
        condition = (
            (j == 1) or(j == 5) or(i == 4 and j <= 4) )
            
        if condition:
            print("* ", end="")
        else:
            print("  ", end="")

    print("", end="")

    for j in range(1, n + 1):
        condition = (
            (j == 1) or (j == 5) or(i == 1 and j <= 4) or (i == 4 and j <= 4) )
           
        if condition:
            print("* ", end="")
        else:
            print("  ", end="")

    print("", end="")

    for j in range(1, n + 1):
        condition = ((j == 1) or(j == 6) or(i == j and i <= 5) )
            
        if condition:
            print("* ", end="")
        else:
            print("  ", end="")

    print()