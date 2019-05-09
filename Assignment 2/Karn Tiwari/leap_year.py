#taking the input
d=int(input("enter the day from 1 to 31:"))
m=int(input("enter the month from 1 to 12:"))
y=int(input("enter the year:"))

#checking for leap year
if y%4==0 and d==29 and m==2:
    if y%100==0:
        if y%400==0:
            print("TRUE")
            
        else :
            print("FALSE")
    else :
        print("TRUE")
        
else:
    print("FALSE")
