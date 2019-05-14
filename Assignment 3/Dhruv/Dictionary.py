a= int(input("How many number yoh want to add for 1 dict\n"))
b={}
for i in range(0,a):
	b.update({i:int(input("Enter number"))})
c= int(input("How many number yoh want to add for 2 dict\n"))
d={}
for i in range(0,c):
	d.update({i:int(input("Enter number"))})
e={}
max=c
min=a
if(c<a):
	max=a
	min=c
for i in range(0,min):
	e.update({i:b[i]+d[i]})
if(c<a):
	for i in range(min,max):
		e.update({i:b[i]})
else:
	for i in range(min,max):
		e.update({i:d[i]})
print("Your first dictionary",b)
print("Your second dictionary",d)
print("Finle dict",e)
