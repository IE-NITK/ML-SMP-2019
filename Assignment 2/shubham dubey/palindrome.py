Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s=input()
n=len(s)
j=n-1
flag=0
for i in range ((int)(n/2)):
    if(s[i]!=s[j]):
        flag=1
        print("0")
        break
    j=j-1
if(flag==0):
        print("1")
