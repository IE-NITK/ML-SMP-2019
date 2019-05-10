#binary Search
def Binary(a,x,f,l):
	if f <= l:
		m = int((l+f)/2)
		if x == a[m]:
			print("Search element " + str(x) + " found at " + str(m))
		elif x > a[m]:
			return Binary(a,x,m+1,l)
		elif x < a[m]:
			return Binary(a,x,f,m-1)
		else:
			print("Search element not found ")
	else:
		print("element not found")



n = int(input("Enter the number of elements in the array : "))
a = list()
print("Enter the list of integers in increasing order : ")
for i in range(n):
	l = int(input("num " + str(i+1) + ": "))
	a.append(l)
print(a)

x = int(input("Enter the search element : "))
Binary(a,x,0,n-1)
