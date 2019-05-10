#!/usr/bin/env python
# coding: utf-8

# In[9]:


def is_leap_baby(day, month, year):
       if day==29 and month=='Feb':
           if (year%4==0):
               if(year%100==0):
                   if(year%400==0):
                       return True
                   else:
                       return False
               return True
       return False
   
a=is_leap_baby(29, "Feb", 1996)
print(a)


# In[ ]:




