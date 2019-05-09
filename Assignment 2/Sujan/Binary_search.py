

l=[23,43,12,43,54,23,76,11,12]
x=int(input("Enter"))

for i in range(len(l)):
    for j in range(0,len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
            
le=0
ge=len(l)

while(le<ge):
    mid=int((le+ge)/2)
    if(x==l[mid]):
        print (mid)
        break
    elif (x<l[mid]):
        ge=mid-1
    else :
        le=mid+1
        
    

    
        
    
