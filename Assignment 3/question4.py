d1={'x':10,'y':20,'z':30}
d2={'x':30,'y':20,'t':40}


for i in d1:
    if i in d2:
        d1[i]=d1[i]+d2[i]
        d2.pop(i)
for i in d2:
    d1[i]=d2[i]
print(d1)
