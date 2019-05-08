a=input("Enter");f=-1;
for i in  range((int)(len(a)/2)):
    if a[i]==a[len(a)-i-1]:
        f=0
        break
print (f)
