s=input("Enter the string")
c=""
for i in s:
    c=i+c
if(c!=s):
     print("-1")
else:
     print("0")
