#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x_min = 115
x_max = 117
x_num = 100

x = np linspace(x_min, x_max, x_ num)
y = normal_distrbution(x,mu,sigma)

dx = (x_max-x_min)/(x_num-1)
prob = 0
for i in range(x_num):
    y = normal_distribution(x[i],mu,sigma)
    prob += y*dx
print("確率:",prob)


# In[ ]:




