myset={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
s=input()
for i in s:
    myset.discard(i)
if len(myset)==0:
    print("Panagram")
else:
    print("Not Panagram")
