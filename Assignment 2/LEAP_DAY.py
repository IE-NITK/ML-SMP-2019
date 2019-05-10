#leap year
def is_leap_baby(d,m,y)
    if d==29:
             if m==Feb or m==feb:
                   if y%4==0 and y%100==0:
                         return 1
                    else:
                           return 0
                else:
                      return 0
      else:
          return 0
d = int(input("Enter the day : "))
m = str(input("Enter the month : "))
y = int(input("Enter the year : "))
n=is_leap_baby(d,m,y)
    if n=0:
      print("It's a leap year")
   elif n=1:
     print("It's not a leap year")
