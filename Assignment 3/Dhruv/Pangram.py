a= input(" Enter string\n")
b=0
for i in range(0,26):
	if(not(chr(97+i) in a)):
		if(not(chr(65+i) in a)):
			b=1
			break
if(b==1):
	print(" string is not pangram")
else:
	print("string is pangram")
