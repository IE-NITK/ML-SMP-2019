import string
se=set( list(string.ascii_lowercase))

i=input("Enter String")

s=set([])

for k in i:
    s.add(k)
    
    
if(s.intersection(se)==se):
    print("pangram")
else:
    print("Not a pangram")
