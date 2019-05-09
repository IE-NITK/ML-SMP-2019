def Binary_search(data,list):
    min=0
    max=len(list)-1
    mid=int((min+max)/2)
    
    while(min<=max):
        mid=int((min+max)/2)
        if(list[mid]==data):
            return True
        if (data<list[mid]):
            max=mid-1
        else:
            min=mid+1
    return False      
list=[1,2,3,4,5,6,7,8,9,10]
if(Binary_search(-1,list)):
   print("found")
else:
   print("not found")
if(Binary_search(10,list)):
   print("found")
else:
   print("not found")        
        

