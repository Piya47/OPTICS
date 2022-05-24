# -*- coding: utf-8 -*-
"""
Created on Sat May 14 00:57:17 2022

@author: User
"""

##OPTICS ASSIGNMENT 2
import numpy as np
import math

# silica
s_A1 = 0.6961663      # refractive index calculate using sellmeier equation from assignment 1
s_A2 = 0.4079426      
s_A3 = 0.8974794
s_B1 = 0.0684043
s_B2 = 0.1162414
s_B3 = 9.896161
x = 0.5               # assume silica with wavelength 0.5micro 
L = 3                 # thickness from lecture note
R1 = 30
R2 = np.inf 
n = 1                 # in air
# nl = math.sqrt(nl_silica)
# sellmeier equation
print('From sellmeier equation')
nl_silica = 1 + ((s_A1*x**2)/(x**2 - s_B1**2)) + ((s_A2*x**2)/(x**2 - s_B2**2)) + ((s_A3*x**2)/(x**2 - s_B3**2))
nl = math.sqrt(nl_silica)
print('nl = ' +str(nl))
print('\n')

#1. Translation matrix
T_matrix = np.array([[1,L],
                    [0,1]])

print('Translation matrix' +'\n' +str (T_matrix))
print('\n')

#2. Refraction at a spherical interface
a2 = 1
b2 = L
c2 = (n-nl)/(R2*nl)
d2 = n/nl

Refrac_matrix = np.array([[a2,b2],
                         [c2,d2]])

print('Refraction at a spherical interface ='+ '\n' +str (Refrac_matrix))
print('\n')

#3. Reflection at a spherical surface
a3 = 1
b3 = 0
c3 = 2/R1
d3 = 1

Reflec_matrix = np.array([[a3,b3],
                         [c3,d3]])

print('Reflection at a spherical surface ='+ '\n' +str (Reflec_matrix))
print('\n')

#calculate the matrix for a thick lens

M = np.matmul(T_matrix,Refrac_matrix,Reflec_matrix)
print('matrix for a thick lens ='+ '\n'+ str(M))       


