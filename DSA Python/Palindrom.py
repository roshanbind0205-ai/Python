p=121
temp=p
rev=0
while(p>0):
    rev=rev*10+(p%10)
    p=p//10
if(temp==rev):
    print("Palindrom")
else:
    print("not palindrom")