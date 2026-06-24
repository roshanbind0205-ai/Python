def check_time():
    

    hour=int(input("Enter the hour : "))
    minute=int(input("Enter the minutes : "))
    second=int(input("Enter the second : "))

    if(hour<0 or hour>23):
        print("Hour error",hour)
        return
    
    if(minute<0 or minute>59):
        print("Minute error",minute)
        return

    if(second<0 or second>59):
        print("Second error",second)
        return
    
    print("Time is Correct : ",hour,":" ,minute,":" ,second)

    if(hour>=13):
        print(hour-12,":" ,minute ,":" ,second, "PM")
        return
    
    if(hour<=11):
        print(hour,":", minute ,":", second, "AM")
        return

    if(hour==12):
        print(hour,":",minute,":",second ,"PM")
        return
    

  
check_time()