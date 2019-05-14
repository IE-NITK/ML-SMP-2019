#!/usr/bin/env python
# coding: utf-8

# In[4]:


def rev(s):
    return s[::-1]

def Palindrome(s):
    reverse=rev(s)
    
    if(s == reverse):
        return 1
    return -1

s="malayalam"
a=Palindrome(s)
print(a)
        


# In[ ]:




