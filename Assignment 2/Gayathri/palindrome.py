#Program to check if a given word is Palindrome
def Palindrome(s):
	for i in range(0,int(len(s)/2)):
		if s[i] != s[len(s)-i-1]:
			return -1
		else:
			return 0
s = input("Enter a String : ")
n = Palindrome(s)
if n == 0:
	print("Palindrome")
else:
	print("Not a Palindrome")	
