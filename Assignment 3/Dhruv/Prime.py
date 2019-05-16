a=int(input("Enter upper limit\n"))
j=2
b={i for i in range(2,a)}
for i in range(2,10):
	b=b.difference({ i*j for j in range(2,int(a/j))})
print("Prime number upto that limit ",b)
	
