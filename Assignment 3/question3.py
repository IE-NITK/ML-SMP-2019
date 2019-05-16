Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list1=[1,2,3,4,5]
list2=[2,3,5]

n1=len(list1)
n2=len(list2)
j=0
for i in range(0,n1):
    if  list1[i]==list2[0]:
        break;
for j in list2:
    if j!=list1[i]:
        print("Not ",end=' ')
        break;
    i+=1
print('sublist')
