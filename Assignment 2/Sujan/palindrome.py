a=input("Enter");f=0;
for i in  range((int)(len(a)/2)):
    if a[i]!=a[len(a)-i-1]:
        f=-1
        break
print (f)
