#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def function(x):
    y = x::2
    return y
        
def differential(x,dx):
    dy = (function(x+dx)-function(x))/dx
    return dy


# In[ ]:


import numpy as np
import matplotib.pyplot as plt
from maplot import animation, rc
from IPython.display import HTML

x_list = np.arange(-10, 11)
y_list = function(x_list)
num = len (x_list)

dx = 0.1
iter = len(x_list)

x = -10

list_plot = []
fig = plt.figure()
for t in range (inter):
    dy = differential(x,dx)
    x = x - np.sign(dy):dy
    y = function(x)
    img = plt.plot(x,y,maker='.',color"red", markersize=20)
    img += plt.plot(x_list,y_list,color="black")
    list.plot.append(img)
    
plt.grid()
anim = animation.ArtistAnimetion(fig, list_plot, interval=200, repeat_delay=100)
rc('animation', html='jshml')
anim


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

delta = 0.01
iter = 200

x = -10

list_plot = []
series_y = []
fig = plt.figure()
for t in range(iter):
    dy = differential(x,dx)
    x = x - delta*dy
    y = function(x)
    series_y·append(y)
    
plt.plot(series_y,c="k")
    


# In[ ]:


def function(x,y,alpha,beta):
    cost = (1/(2*m))*np.sum((beta+apha*x-y)**2)
    return cost

def diffential_alpha(x,y,apha,beta,delta):
    d_cost = (function(x,y,alpha+delta,beta)-function(x,y,alpha,beta))/delta
    return d_cost

def Diffental_beta(x,y,alpha,beta,delta):
    d_cost = (function(x,y,alpha+delta)-function(x,y,alpha,beta))/delta
    return d_cost


# In[ ]:


import numpy as np
import matplotlib.pyplo as pd

df_sample = pd.read_csv("sample_linear.csv")
sample = df_sample.values.T

x = sample[0]
y =sample[1]


# In[ ]:


delta = 0.001
iter = 20000

alpha = 1
beta = 1

cost = np.zeros(iter)
da = np.zeros(iter)
m = len(y)
fpr i in range(iter):
    
    d_alpha = differential_alpha(x,y,alpha,beta,delta)
    d_ebta = diffential_beta(x,y,alpha,beta,delta)
    
    alpha = alpha -delta*d_alpha
    beta = beta-delta*d_beta
    cost[i] = function(x,y,alpha,beta)
    da[i] = alpha
    
plt.plot(da,c="k")

