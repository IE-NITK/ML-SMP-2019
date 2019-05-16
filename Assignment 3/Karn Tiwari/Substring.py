# -*- coding: utf-8 -*-
"""
Created on Thu May 16 09:59:25 2019

@Author: Karn Tiwari
"""
#taking list1 as input
x=int(input("Enter the Number of Elements in Test_List: "))
test_list=[]
print("Enter the Test_List Elements: ")
for i in range(x):
    p=input()
    test_list.append(p)
print(test_list)

#taking list2 as input
y=int(input("Enter the Number of Elements in Sub_List: "))
sub_list=[]
print("Enter the Sub_List Elements: ")
for i in range(y):
    p=input()
    sub_list.append(p)
print(sub_list)

#Algorithm for checking substring   
flag=0
if x>=y:
    for j in range(x-y+1):
        if sub_list[0]==test_list[j] and j+y<=x and sub_list[0:y]==test_list[j:j+y]:
            flag=1
            break
                
    if flag==1:
        print("TRUE")
    else:
        print("FALSE")

else:
    print("FALSE")
