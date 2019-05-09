1 st question
a=input("enter word\n")
b=len(a)
int(b)
c=0
for i in range(0,b-1):
	if(a[i]!=a[b-i-1]):
		c=1
		break
if(c==0):
    print("Word is palindrom")
else:
	print("Word is not palindrom")

2 nd question
print("Enter your birth day")
c=0
e=0
f=0
g=0
while(g!=1):
	a=int(input())
	if(a>31):
		print("Enter the day again")
	if(a<=31):
		g=1
if(a==29):
	c=1
g=0
print("Enter your birth month")
while(g!=1):
	b=int(input())
	if(b>12):
		print("Enter the month again")
	if(b<=12):
		g=1
if(b==2):
	e=2
print("Enter your birth year")
d=int(input())
if(d%100==0):
	if(d%400==0):
		f=3
else:
	if(d%4==0):
		f=3
if(c==1 and e==2 and f==3):
	print("Baby is leap year baby")
else:
	print("Baby is not leap year baby")

3 rd question

print("How many number you want to add")
a=int(input())
b=[]
print("Enter the numbers in increasing order")
for i in range(0,a):
	b.append(int(input()))
print("Enter the element which you eant to search")
c=int(input())
d=0
f=0
e=a-1
while(e>=d):
	m=int((e+d)/2)
	if(b[m]==c):
		f=1
		break
	if(b[m]<c):
		d=m+1
	if(b[m]>c):
		e=m-1
if(f==1):
	print("Element is found")
else:
	print("Element is not found")

4th question
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
		c=c+a[i][j]
	if(c!=(n*(n+1)/2)):
		d=1
		break
	c=0
if(d==1):
	print("Your given matrix is not perfect sudoku")
else:
	print("Matrix is perfect sudoku") 
