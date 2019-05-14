def check_sudoku(a):
#case 1
	flag = 0
	for i in range(n):
		for j in range(n):
			for k in range(j+1,n):
				if a[i][j] == a[i][k]:
					flag = 1
					break
	if flag == 1:
		return -1
	else:
		print("row-wise correct input")
#case 2
	flag = 0
	for i in range(n):
		for j in range(n):
			for k in range(j+1,n):
				if a[i][j] == a[k][i]:
					flag = 1
					break
	if flag == 1:
		return -1
	else:
		print("column-wise correct")
#case 3
	flag = 0
	for i in range(n):
		for j in range(n):
			if a[i][j] > n or a[i][j] == 0:
				flag = 1
				break
	if flag == 1:
		return -1
	else:
		print("All numbers in the correct range")









n = int(input("Enter the number of rows and columns in the square input : "))
a = []
for i in range(n):
	row = []
	for j in range(n):
		row.append(int(input("row " + str(i+1) + " column " + str(j+1) + " : "))) 
	a.append(row)
print(a)
result = check_sudoku(a)
if result == -1:
	print("Error")


