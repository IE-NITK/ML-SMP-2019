def binarySearch(ar, x):
    r = n-1
    l = 0
    while l <= r:
        mid = l +(r-l)//2
        if ar[mid] == x:
            return mid
        elif ar[mid] < x:
            l = mid +1
        else:
            r = mid -1
    return -1
n = int(input("Enter no of element in list : "))
a = []
print("Enter elements")
for i in range(0,n):
    e = int(input())
    a.append(e)
a.sort()
x = int(input("Element to be search : "))
pos = binarySearch(a, x)
if pos != -1: 
    print("Element is present at index %d in sorted list" % (pos+1) )
else: 
    print("Element is not present in array")