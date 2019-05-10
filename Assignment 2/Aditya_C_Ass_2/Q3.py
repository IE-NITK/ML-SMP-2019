#!/usr/bin/env python
# coding: utf-8

# In[20]:


def bs(arr, l, r, x):
    if(r>=1):
        mid=int((l+(r))/2)
        
        if(arr[mid]==x):
            return mid
        
        elif(arr[mid]>x):
            return bs(arr, l, mid-1, x)
        
        else:
            return bs(arr, mid+1, r, x)
    else:
        return -1
    
arr=[5, 4, 3, 10, 20]
x=3

a=bs(arr, 0, len(arr)-1, x)

print(a)


# In[ ]:




