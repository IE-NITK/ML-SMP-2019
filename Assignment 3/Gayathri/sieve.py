import math

n = int(input("Enter the a number upto which primes have to be entered : "))

p = []
for i in range(2,n+1):
    p.append(i)

i = 2
while(i <= int(math.sqrt(n))):
    if i in p:
        for j in range(i*2, n+1, i):
            if j in p:
                p.remove(j)
    i = i+1
print(p)
