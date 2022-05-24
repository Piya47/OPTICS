# -*- coding: utf-8 -*-
"""
Created on Sat May 14 00:50:32 2022

@author: User
"""
#OPTICS ASSIGNMENT 1.2
import numpy as np
import math 
import matplotlib.pyplot as plt

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

#s'= image
#s= object
n1 = 1
#n2 = refractive index of silicon and MgF2
# if R2 is positive the surface is concave, and if R2 is negative the surface is convex
# i choose R2 negative for convex, so the graph look nice 
S = 40
R11= 20
R12= -20

R21= 10
R22= -30

R31= 20
R32= np.inf 

nsilica = []  
nmgf2 = [] 
imageS1 = [] 
imageS2 = []
imageS3 = []

imageM1 = []
imageM2 = []
imageM3 = []

for x in lamb:
  n_silica = 1 + ((silica_A1*x**2)/(x**2 - silica_B1**2)) + ((silica_A2*x**2)/(x**2 - silica_B2**2)) + ((silica_A3*x**2)/(x**2 - silica_B3**2))
  n_mgf2 = 1 + ((mgf2_A1*x**2)/(x**2 - mgf2_B1**2)) + ((mgf2_A2*x**2)/(x**2 - mgf2_B2**2)) + ((mgf2_A3*x**2)/(x**2 - mgf2_B3**2))
  nsilica.append(n_silica)
  nmgf2.append(n_mgf2)
#print('Refrective index Silica=')
#print(nsilica)
#print('N Mgf2=')
#print(nmgf2)

for n2 in nsilica : #arr
  A = 1/(((math.sqrt(n2)-n1)/n1)*(1/R11-1/R12)-1/S)      #image_silica_1
  B = 1/(((math.sqrt(n2)-n1)/n1)*(1/R21-1/R22)-1/S)      #image_silica_2
  C = 1/(((math.sqrt(n2)-n1)/n1)*(1/R31-1/R32)-1/S)      #image_silica_3
  imageS1.append(A)
  imageS2.append(B)
  imageS3.append(C)

print('images silica ')
print(imageS1)
print(imageS2)
print(imageS3)

for n3 in nmgf2: #n3 is n2 of MgF2
  D = 1/(((math.sqrt(n3)-n1)/n1)*(1/R11-1/R12)-1/S)      #image_mgf2_1
  E = 1/(((math.sqrt(n3)-n1)/n1)*(1/R21-1/R22)-1/S)      #image_mgf2_2
  F = 1/(((math.sqrt(n3)-n1)/n1)*(1/R31-1/R32)-1/S)      #image_mgf2_3
  imageM1.append(D)
  imageM2.append(E)
  imageM3.append(F)

print('images MgF2 ')
print(imageM1)
print(imageM2)
print(imageM3)

# GRAPH SILICA IMAGES FOR 1,2,3
plt.plot(lamb,imageS1, color= 'b')
plt.title('GRAPH SILICA IMAGES NUMBER 1')
plt.xlabel('Wavelength')
plt.ylabel('Images Silica Number 1', color ='b')
plt.show()

plt.plot(lamb,imageS2, color= 'b')
plt.title('GRAPH SILICA IMAGES NUMBER 2')
plt.xlabel('Wavelength')
plt.ylabel('Images Silica Number 2', color ='b')
plt.show()

plt.plot(lamb,imageS3, color= 'b')
plt.title('GRAPH SILICA IMAGES NUMBER 3')
plt.xlabel('Wavelength')
plt.ylabel('Images Silica Number 3', color ='b')
plt.show()

#GRAPH MgF2 IMAGES FOR 1,2,3
plt.plot(lamb,imageM1, color= 'g')
plt.title('GRAPH MgF2 IMAGES NUMBER 1')
plt.xlabel('Wavelength')
plt.ylabel('Images MgF2 Number 1', color ='g')
plt.show()

plt.plot(lamb,imageM2, color= 'g')
plt.title('GRAPH MgF2 IMAGES NUMBER 2')
plt.xlabel('Wavelength')
plt.ylabel('Images MgF2 Number 2', color ='g')
plt.show()

plt.plot(lamb,imageM3, color= 'g')
plt.title('GRAPH MgF2 IMAGES NUMBER 3')
plt.xlabel('Wavelength')
plt.ylabel('Images MgF2 Number 3', color ='g')
plt.show()


