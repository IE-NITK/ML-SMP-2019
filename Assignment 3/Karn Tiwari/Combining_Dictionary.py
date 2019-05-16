#taking Dictionary1 Key and Value
D1={}
print("Enter the number of element in Dictionary1: ")
n1=int(input())
print("Enter the key and value (with space b/w them) in Dictionary1: ")
D1=dict(input().split() for x in range(n1))
print(D1)

#taking Dictionary2 Key and Value
D2={}
print("Enter the number of element in Dictionary2: ")
n2=int(input())
print("Enter the key and value (with space b/w them) in Dictionary2: ")
D2=dict(input().split() for x in range(n2))
print(D2)

#taking intersection of Dictionary1 and Dictionary2
D3={}
for key in D1:
    if key in D2:
        D3[key]=int(D1[key]) + int(D2[key])

for key in D1:
    if key not in D3:
        D3[key]=int(D1[key])
        
for key in D2:
    if key not in D3:
        D3[key]=int(D2[key])

#Printing result 
print(D3)
