word = input("Enter the word or phrase : ")

l = len(word)
f = 0

for i in range(0,l//2 - 1):
    if(word[i] != word[l-1-i]):
        f = -1
        break

print(f)