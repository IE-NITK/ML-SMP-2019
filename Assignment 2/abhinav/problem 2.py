dd=int(input("Enter the date : "))
mm=int(input("Enter the month : "))
yyyy=int(input("Enter the year"))
if(dd==29):
    if(mm==2):
        if((y%100)%4==0):
            if(y%400==0):
                print("given year is a leap year:")
else:
    print("Not a leap year")        
