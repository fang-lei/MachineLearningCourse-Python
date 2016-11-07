
# coding: utf-8

# Exercise 01

# Q1: distribution P(x,y)

# In[12]:

import numpy
import matplotlib
import math
get_ipython().magic('matplotlib inline')
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
R = numpy.arange(-4,4+1e-9,0.1)
x,y = numpy.meshgrid(R,R)


# Define the probability function (discrete)

# In[11]:

z = sum(sum(math.e**(-0.5*(x**2+y**2))))
F = 1/z*math.e**(-0.5*(x**2+y**2))
fig = plt.figure(figsize=(10,6))
ax = plt.axes(projection='3d')
ax.scatter(X,Y,F,s=1,alpha=0.5)


# Q2: conditional distribution

# In[15]:

z = sum(sum(math.e**(-0.5*(x**2+y**2))))
F = 1/z*math.e**(-0.5*(x**2+y**2))
Fcon = F*((x**2+y**2)**0.5>=1)
Fcon1 = Fcon/Fcon.sum()
fig = plt.figure(figsize=(10,6))
ax = plt.axes(projection='3d')
ax.scatter(X,Y,Fcon1,s=1,alpha=0.5)


# Q3: Marginal distribution

# In[ ]:




# In[ ]:




# In[ ]:



