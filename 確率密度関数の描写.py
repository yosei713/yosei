#!/usr/bin/env python
# coding: utf-8

# In[ ]:


mu = 116.6
sigma = 4.8

x_min = 80
x_max = 159
x_num = 100

x = np.linspace(x_min, x_max, x_num)
y = normal_distbution(x,mu,sigma)

plt.plot(x, y ,color="k")
plt.show()
get_ipython().run_line_magic('matplotlib', 'inline')

