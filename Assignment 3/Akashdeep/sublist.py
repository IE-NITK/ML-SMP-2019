#!/usr/bin/env python
# coding: utf-8

# In[6]:


a = []
n = int(input("Enter size "))
for i in range(n):
    e = int(input())
    a.append(e)
s = str(input("Enter sublist"))
b = s.split()
m = len(b)
for i in range(m):
    b[i] = int(b[i])
for i in range(n):
        if b == a[i:i+m]:
            m = -1
            print("sublist at",i,"position")
if m != -1:
    print("sublist not found")

