choose=int(input("1.Tuple\n2.List\n3.Set\n4.Dictionary\n5.Frozen Set\nChoose Number : "))


if choose==1:
    data=(1,4,3,2,5)
    print(data)
    print(type(data))

elif choose==2:
    a=[4,9,33,22]
    print(a)
    print(type(a))

elif choose==3:
    s={33,2,33,89}
    print(s)
    print(type(s))

elif choose==4:
      d={
           "name":"Roshan Bind",
           "email":"roshanbind0205@gmail.com",
           "mobile":8188935865
      } 

      print(d)
      print(type(d))

elif choose==5:
     f=frozenset({2,3,1,3,2,1,4})
     print(f)
     print(type(f))

else:
    print("Invalid Number")