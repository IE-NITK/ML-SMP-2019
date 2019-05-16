#Program to find if a list is a sublist of an other list
def issubset(n,m,parent_list,test_list):
	if n<m:
		print("This is not a subset")
	elif n>m:
		flag = 0
		for i in range(0,n):
			if test_list[0] == parent_list[i]:
				flag = 1
				break
		n = i
		print(n)
		if flag == 0:
			print("test_set is not a subset of parent_set")
		elif flag == 1:
			flag1 = 0
			for i in range(1,m):
				if test_list[i] != parent_list[n+i]:
					flag1 = 1
			if flag1 == 1:
				print("not a subset")
			else:
				print("It's a subset")		

parent_list = []
n = int(input("Enter the number of elements to beentered in the list : "))
print("Enter the elements of the parent list one below the other")
for i in range(0,n):
	l = int(input("Element " +str( i+1 ) + ": "))
	parent_list.append(l)
print(parent_list)

m = int(input("Enter the number of elements to be entered in the test list : "))
test_list = []
for i in range(0,m):
	l = int(input("Element " +str( i+1 ) + ": "))
	test_list.append(l)
print(test_list)
issubset(n,m,parent_list,test_list) 

