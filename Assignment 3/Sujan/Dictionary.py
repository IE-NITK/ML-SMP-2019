d1={'x':10,'y':20,'z':30}
d2={'x':30,'y':20,'t':40}

d3={}

for i in d1.keys():
    d3[i]=d1[i]
    
for i in d2.keys():
    if i in d3.keys():
        d3[i]+=d2[i]
    else:
        d3[i]=d2[i]
        
print(d3)
        
