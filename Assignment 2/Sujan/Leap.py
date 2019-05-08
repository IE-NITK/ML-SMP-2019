
def leap(a,b,c):
    if(c%4==0 and c%100!=0 and b=='Feb' and a==29):
        return True
    else :return False


a=int(input("Enter day"))

b=input('enter month')
c=int(input('enter year'))
print (leap(a,b,c))


    
        
    
