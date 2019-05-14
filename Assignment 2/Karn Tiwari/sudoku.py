#to take input for square size and array element
n=int(input("enter the size of square greater than 1 :"))
arr=[[0 for col in range (n)] for row in range(n)]
brr=[[0 for col in range (n)] for row in range(n)]

print("enter the element of 2D array:")

for r in range(n):
    for c in range(n):
        x=int(input())
        arr[r][c]=x
 
#printing array element       
print(arr)

#creating array with column and row interchanged 
for i in range(n):
    for j in range(n):
        brr[i][j]=arr[j][i]

#checking for each element value and occurance of number in a row
y=0 
z=0
for i in range(n):
    for j in range(n):
        if arr[i][j]>n:
            y=1
            break
        elif arr[i][j]<=0:
            y=1
            break
    if y==1:
        break
    else:
        for j in range(n):
            for k in range(j+1,n):
                if arr[i][j]==arr[i][k]:
                    z=1
                    break
            if z==1:
                break
    if z==1:
        break
    
#checking for each element value and occurance of number in a column
 
q=0
for i in range(n):
    for j in range(n):
            for k in range(j+1,n):
                if brr[i][j]==brr[i][k]:
                    q=1
                    break
            if q==1:
                break
    if q==1:
        break
        
if y==0 and z==0 and q==0:
    print("TRUE")
else:
    print("FALSE")
