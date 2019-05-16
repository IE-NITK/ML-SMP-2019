i=input("enter number")
a=int(i)

l=list(range(2,a+1))

k=2



while(l.index(k)!=(len(l)-1)):
    for i in l:
      if(i%k==0 and i!=k):
          l.remove(i)

    k=l[l.index(k)+1]


print(l)
