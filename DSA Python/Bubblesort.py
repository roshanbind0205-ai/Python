arr=[5,7,8,10,12,2,1]
for i in range(len(arr)):
    for j in range(len(arr)):
        if(arr[i]< arr[j]):
            
            t=arr[i]
            arr[i]=arr[j]
            arr[j]=t
for i in range(len(arr)):
    print(arr[i],end=" ")
    
