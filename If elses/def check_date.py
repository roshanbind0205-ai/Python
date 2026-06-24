def check_date():
    
    day = int(input("Enter the Day : "))
    month = int(input("Enter the Month : "))
    year = int(input("Enter the Year : "))

    if year<1:
        print("Year Error :", year)
        return

    if month<1 or month>12:
        print("Month Error :", month)
        return

    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        noofdays=31

    else:
        if month==4 or month==6 or month==9 or month==11:
            noofdays = 30

        else:
            if year % 400==0 or (year%4==0 and year%100!= 0):
                noofdays=29
            else:
                noofdays=28

    if day<1 or day >noofdays:
        print("Day Error :", day)
        return

    print("Date is Correct :", day, month, year)


check_date()