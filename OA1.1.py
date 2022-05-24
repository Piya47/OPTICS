# -*- coding: utf-8 -*-
"""
Created on Sat May 14 00:18:46 2022

@author: User
"""

#OPTICS ASSIGNMENT 1.1

import numpy as np
from sympy import Eq
import matplotlib.pyplot as plt

##############
# n = refractive index
# lambda= wavelength
# axis lambda = 0.4-1.0microm
# n(lambda)^2 = 1 + sum(n) {A*lambda^2/(lambda^2-B^2)}
# (A,B)
##############

lamb = np.arange(0.4,1.001, 0.001)

silica_A1 = 0.6961663
silica_A2 = 0.4079426
silica_A3 = 0.8974794
silica_B1 = 0.0684043
silica_B2 = 0.1162414
silica_B3 = 9.896161
mgf2_A1 = 0.48755108
mgf2_A2 = 0.39875031
mgf2_A3 = 2.3120353
mgf2_B1 = 0.04338408
mgf2_B2 = 0.09461442
mgf2_B3 = 23.793604
#axs = plt.subplots(2)
arr = []
arr1 = []

for x in lamb:
  n_silica = 1 + ((silica_A1*x**2)/(x**2 - silica_B1**2)) + ((silica_A2*x**2)/(x**2 - silica_B2**2)) + ((silica_A3*x**2)/(x**2 - silica_B3**2))
  n_mgf2 = 1 + ((mgf2_A1*x**2)/(x**2 - mgf2_B1**2)) + ((mgf2_A2*x**2)/(x**2 - mgf2_B2**2)) + ((mgf2_A3*x**2)/(x**2 - mgf2_B3**2))
  arr.append(n_silica)
  arr1.append(n_mgf2)

print(arr)
print(arr1)
print('\n')
plt.plot(lamb,arr, color= 'b')
plt.title('Graph Refrective index of Silica versus Wavelength')
plt.xlabel('Wavelenghth (Lambda)')
plt.ylabel('Refrective index of Silica', color ='b')
plt.show()
print('\n')

plt.plot(lamb,arr1, color= 'r')
plt.title('Graph Refrective index of Mgf2 versus Wavelength')
plt.xlabel('Wavelenghth (Lambda)')
plt.ylabel('Refrective index of MgF2', color ='r')
plt.show()

print('\n')

### GRAPH PLOT COMBINE
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
graph1 = ax1.plot(lamb,arr, label=' Refrective index Silica',  color= 'b')
graph2 = ax2.plot(lamb,arr1, label= 'Refrective index MgF2', color= 'r')
plt.title('Graph Refrective index of Silica and MgF2 versus Wavelength')
ax1.set_xlabel('Wavelenghth (Lambda)')
ax1.set_ylabel('Refrective index Silica', color='b')
ax2.set_ylabel('Refrective index MgF2', color='r')
plt.plot()
plt.show()



#ax1.set_title("Graph lambda againts silica")
#ax1.plot(lamb, arr)
#ax2.set_title("Graph lambda againts mgf2")
#ax2.plot(lamb, arr1)
#plt.plot(lamb,arr)
#plt.plot(lamb,arr1)
#plt.show()