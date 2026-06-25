n = 5

for i in range(n):
    for j in range(2 * n - 1):
        if j == n - i - 1 or j == n + i - 1 or (i == n // 2 and j > n - i - 1 and j < n + i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
    