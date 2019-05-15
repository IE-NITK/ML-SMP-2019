#!/usr/bin/env python
# coding: utf-8

# In[33]:


d1 = {'x': 10, 'y': 20, 'z':30}
d2 = {'x': 30, 'y': 20, 't':40}
for k,v in d1.items():
    if(k in d2):
        d2[k] += v
    else : d2[k] = v
        
print(d2)
    

