#pallindrome
def pallindrome(s):
      for i in range (0,int(len(s)/2)):
                if s(i)!=s(len-i-1):
                      return -1
                else :
                      return 0
s=input("Enter a string")
n=pallindrome(s)
if n==0:
       print("The string is a pallindrome")
else:
       print("Not a pallindrome")
