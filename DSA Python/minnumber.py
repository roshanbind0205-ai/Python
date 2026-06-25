a=[4,6,8,4,7,8]
min=a[0]
for i in range(len(a)):
    if(min>a[i]):
        min=a[i]
print("min :",min)