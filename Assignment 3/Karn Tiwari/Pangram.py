#taking string as input
print("Enter the String: ")
string=input()

#variable declaration and initialization
string=string.lower()
a=[0 for i in range(0,26)]
x=len(string)

#Algorithm for pangram
for i in range(x):
    flag=0
    for j in range(i+1,x):
        if string[j]==string[i]:
            flag=1
            break
    if flag==0:
        for k in range(97,123):
            if chr(k)==string[i]:
                a[k-97]+=1       
flag=0
for i in range(26):
    if a[i]==0:
        flag=1
        break
    
#printing result
if flag==0:
    print("The Given String is Pangram !")
else:
    print("The Given String is not Pangram !")
