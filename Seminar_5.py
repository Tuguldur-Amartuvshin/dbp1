#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[4]:


#1
n = int(input())
for i in range(0,n+1):
    print('*'*i)


# In[13]:


#2
n = int(input())
for i in range(0,n+1):
    a = ['*'*i]
    for k in a:
        print(k)


# In[21]:


#3
students = {'Bat': 18, 'Oyun': 22,'Dulam': 21,'Suren': 20}
def max_dict(x):
    max_min = [max(x, key=x.get ),min(x, key=x.get)]
    return max_min
l = max_dict(students)
for i in l:
    print(i)
    


# In[20]:


#4
import numpy as np
x = np.arange(1,1000)
a = 0
for i in x:
    if ((i % 3) == 0 | (i % 7) == 0):
        a = a+ i
print(a)


# In[ ]:




