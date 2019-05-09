#4th question
print("Enter the size of square matrix")
n=int(input())
a=[]
print("enter th e matrix elements less then size ",n+1)
for i in range(0,n):
	b=[]
	for j in range(0,n):
		b.append(int(input()))
	a.append(b)
c=0
d=0
print(a)
for i in range(0,n):
	for j in range(0,n):
		if(a[i][j]>n or a[i][j]==0):
			d=1
			break
		for k in range(0,n):
			if(a[i][j]==a[i][k] and (j!=k)):
				d=1
				break
			if(a[i][j]==a[k][j] and (i!=k)):
				d=1
				break
if(d==1): 
	print("Your given matrix is not perfect sudoku or your input is wrong")
else:
	print("Matrix is perfect sudoku") 
