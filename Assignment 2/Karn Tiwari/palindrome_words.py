#taking word as input
word=input("enter the word : ")
word=word.lower()

#calculating word length
x=len(word)

#checking for palindrome
for i in range(0,int(x/2)):
    if word[i]==word[x-i-1]:
        y=1
    else:
        y=0
        break

#printing the result
if y==1:
    print(0)
else :
    print(-1)
