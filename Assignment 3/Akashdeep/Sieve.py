#!/usr/bin/env python
# coding: utf-8

# In[4]:


a = []
l = int(input("Enter limit "))
for i in range(l):
    a.append(True)
for i in range(2,l):
    if a[i]:
        for j in range(i*i,l,i):
            a[j] = False
for i in range(2,l):
    if a[i]:
        print(i)

