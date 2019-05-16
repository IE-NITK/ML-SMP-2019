#Taking Input Number N
n=int(input('Enter the Number for finding Prime number upto that Number: '))

#Initializing Array with 0
arr=[0 for i in range(n+1)]
arr[0]=1
arr[1]=1

#Sieve of Eratosthenes Algorithm
for i in range(2,int(n**0.5)+1):
    if arr[i]==0:
        for j in range(i*2,n+1,i):
            arr[j]=1

#Printing Prime Numbers upto N
count=0
for i in range(n+1):
    if arr[i]==0:
        print(i,end=" ")
        count+=1
    
#Printing Number of Prime Numbers upto N
print("\n","The number of Prime Number upto",n,"are: ",count)
