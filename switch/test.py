choose= int (input(" 1.Tuple\n 2.list\n 3.set\n 4.dictionary\n 5.frozen set\n 6. Choose Number :"))

if choose==1:
    data=[1,4,5,]
    print(data)
    print(type(data))
    
elif choose==2:
    a=(1,2,3,1)
    print(a)
    print(type(a))
    
elif choose==3:
    s={1,3,3,2,1}
    print(s)
    print(type(s))
    
elif choose==4:
    d={
        "Name":"Roshan Bind",
        "email":"roshanbind0205@gmail.com",
        "Mobile No":8188935865
    }
    print(d)
    print(type(d))
    
elif choose==5:
    f=frozenset({2,3,1,3,2,1,4})
    print(f)
    print(type(f))
else:
    print("Invalid number")