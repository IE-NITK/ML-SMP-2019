#Program to combine dictionaries 

def getlistk(my_dict):
	return list(my_dict.keys())
def getlistv(my_dict):
	return list(my_dict.values())
n1 = n2 = int(input("Enter the number of pairs to be entered in the dictionaries: "))
print("Enter the pairs of dictionary 1 : ")
my_dict1 = dict(input().split() for i in range(n1))
print("Enter the pairs of dictionary 2 : ")
my_dict2 = dict(input().split() for i in range(n2))


k1 = getlistk(my_dict1)
k2 = getlistk(my_dict2)
v1 = getlistv(my_dict1)
v2 = getlistv(my_dict2)
for i in range(n1):
	for j in range(n2):
		if k1[i] == k2[j]:
				my_dict1[k1[i]]=str(int(v1[i])+int(v2[j]))

	for i in range(n1):
		if k1[i] != k2[i]:
			my_dict1[k2[i]] = v2[i]
print(my_dict1)

			
