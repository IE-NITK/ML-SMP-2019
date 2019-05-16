#To check if the entered string is a pangram
#A pangram is a string that contains all the 26 alphabet atleast once
my_set = set([])
input_string = input("Enter a String that has to be checked for a pangram : ")
for i in input_string:
	my_set.add(i)

alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_set = set([])
for i in alpha:
	alpha_set.add(i)

if (my_set & alpha_set) == alpha_set:	
	print("\nThe String you have entered IS A PANGRAM\n")
else:
	print("\nThe String you have entered IS NOT A PANGRAM\n")
