
l1=(input("enter number seperated by spaces").split(" "))



l2=(input("enter number seperated by spaces").split(" "))

f=0



if(set(l2).issubset(set(l1))):
    ind=l1.index(l2[0])
    j=0
    
    for i in range(ind,ind+len(l2)):
        if(i>=len(l1)):
            f=1
            break
        if(l1[i]!=l2[j]):
            f=1
            
            break
        j+=1
else:
    f=1
    
if(f==0):
    print("sublist")
else:
    print("not")
            
    
