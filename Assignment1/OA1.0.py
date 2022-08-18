# -*- coding: utf-8 -*-
"""
Created on Sat May 14 00:36:06 2022

@author: User
"""

#OPTICS ASSIGNMENT 1.0 BASIC

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,10,0.01)

def f(x): return np.sin(x)
plt.plot(x,f(x))
plt.title('SIN GRAPH')
plt.xlabel('X')
plt.ylabel('Sin(x)', color = 'b')
plt.show()


x = np.arange(1,10,0.01)
def f(x): return np.exp(x)
plt.plot(x,f(x), color= 'r')
plt.title('EXPONENTIAL GRAPH')
plt.xlabel('X')
plt.ylabel('Exp(x)', color ='b')
plt.show()

x = np.arange(1,10,0.01)
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
graph1 = ax1.plot(x,np.sin(x), label = 'Sin(x)', color= 'b')
graph2 = ax2.plot(x,np.exp(x), label = 'Exp(x)', color= 'r')
plt.title('SIN AND EXPONENTIAL GRAPH')
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)', color='b')
ax2.set_ylabel('exp (x)', color='r')

plt.plot()
plt.show()

