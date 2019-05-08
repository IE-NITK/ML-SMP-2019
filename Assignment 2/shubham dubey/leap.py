Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def is_leap(d,m,y):
    if(d==29 and m==2):
        if (y%100!=0 and y%4==0):
            return True
        elif (y%400==0):
            return True
        else:
            return False
d=int(input())
m=int(input())
y=int(input())
if(is_leap(d,m,y)):
    print("yes")
else:
    print("no")
