#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math 
importnumpy as np 
import matplotlib.pyplot as plt 

def normal_distribution(x,mu,sigma):
    y = 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-(x-mu)**2)/(2*sigma**2))
    return y


# In[ ]:




