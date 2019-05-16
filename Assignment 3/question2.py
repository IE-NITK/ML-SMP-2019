n=5
n1=n+1
l=[True] * n1
for i in range(2,n+1):
    if l[i]==True:
        print(i,end=' ')
        for j in range(i**2,n+1,i):
            l[j]=False
