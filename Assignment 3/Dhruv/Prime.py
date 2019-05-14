a=int(input("Enter upper limit\n"))
b=[]
c={i for i in range(2,a)}
j=0
for i in range(2,a):
	b.append(i)
for i in range(2,a):
	for j in range(0,len(b)):
		if(b[j]%i==0):
			if(b[j]!=i):
				 c.discard(b[j])
print("Prime numbers upto that limit ",c)
