arr = [1, 6, 0, 1, 9, 7, 5]
print("Original:", arr)

f = [0] * 10
print("Initial f:", f)

for x in arr:
    f[x] += 1
print("Freq f:", f)

for i in range(1, 10):
    f[i] += f[i - 1]
print("Cumulative f:", f)

n = len(arr)
arry = [0] * n

for i in range(n - 1, -1, -1):
    x = arr[i]
    pos = f[x]
    arry[pos - 1] = x
    f[x] -= 1

print("Sorted:", arry)