#taking the input
d=int(input("enter the number of element in the list:"))
print("enter the list element")
arr=[]
for i in range(d):
    x=int(input())
    arr.append(x)

#sorting of list elements
for i in range(0,d):
    for j in range(i+1,d):
        if arr[i]>=arr[j]:
            t=arr[i]
            arr[i]=arr[j]
            arr[j]=t
            
#input for key element
print("enter the key element ")
key=int(input())
print(arr)

#binary search algorithm
ma=d
mi=0
y=0

while ma>mi:
    mid=int((ma+mi)//2)
    if key==arr[mid]:
        y=1
        p=mid+1
        break
    elif key>arr[mid]:
        mi=mid
    else:
        ma=mid

if y==1:
    print("key element found @ ",p)
else:
    print("key element not found")
