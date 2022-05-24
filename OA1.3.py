# -*- coding: utf-8 -*-
"""
Created on Sat May 14 00:52:28 2022

@author: User
"""
#OPTICS ASSIGNMENT 1.3
import numpy as np
import math 
import matplotlib.pyplot as plt

#---------------------------
#Abbe Number = VD
# Focal length of the blue Fraunhofer F line from Hydrogen = fF   blue
# Focal length of the red Fraunhofer C line from Hydrogen = fC    red
# Focal length of the orange Fraunhofer D line from sodium = fD   orange

n1 = 1
#n2 = n for siilica and Mgf2 in lamb f,c,d
S = 40
R1 = 20
R2 = -20

# wavelength from lecture notes 6
lamb_f = 0.4861   #Blue
lamb_d = 0.5892   #Yellow for orange
lamb_c = 0.6563   #Red

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

# refrective index silica for f,c,d -------------------------------------------------

n_silica_f = 1 + ((silica_A1*lamb_f**2)/(lamb_f**2 - silica_B1**2)) + ((silica_A2*lamb_f**2)/(lamb_f**2 - silica_B2**2)) + ((silica_A3*lamb_f**2)/(lamb_f**2 - silica_B3**2))
nsilica_f = math.sqrt(n_silica_f)
print('N silica f=')
print(nsilica_f)

n_silica_c = 1 + ((silica_A1*lamb_c**2)/(lamb_c**2 - silica_B1**2)) + ((silica_A2*lamb_c**2)/(lamb_c**2 - silica_B2**2)) + ((silica_A3*lamb_c**2)/(lamb_c**2 - silica_B3**2))
nsilica_c = math.sqrt(n_silica_c)
print('N silica c=')
print(nsilica_c)

n_silica_d = 1 + ((silica_A1*lamb_d**2)/(lamb_d**2 - silica_B1**2)) + ((silica_A2*lamb_d**2)/(lamb_d**2 - silica_B2**2)) + ((silica_A3*lamb_d**2)/(lamb_d**2 - silica_B3**2))
nsilica_d = math.sqrt(n_silica_d)
print('N silica d=')
print(nsilica_d)

print('\n')
# refrective index Mgf2 for f,c,d---------------------

n_mgf2_f = 1 + ((mgf2_A1*lamb_f**2)/(lamb_f**2 - mgf2_B1**2)) + ((mgf2_A2*lamb_f**2)/(lamb_f**2 - mgf2_B2**2)) + ((mgf2_A3*lamb_f**2)/(lamb_f**2 - mgf2_B3**2))
nmgf2_f = math.sqrt(n_mgf2_f)
print('N mgf2 f=')
print(nmgf2_f)

n_mgf2_c = 1 + ((mgf2_A1*lamb_c**2)/(lamb_c**2 - mgf2_B1**2)) + ((mgf2_A2*lamb_c**2)/(lamb_c**2 - mgf2_B2**2)) + ((mgf2_A3*lamb_c**2)/(lamb_c**2 - mgf2_B3**2))
nmgf2_c = math.sqrt(n_mgf2_c)
print('N mgf2 c=')
print(nmgf2_c)

n_mgf2_d = 1 + ((mgf2_A1*lamb_d**2)/(lamb_d**2 - mgf2_B1**2)) + ((mgf2_A2*lamb_d**2)/(lamb_d**2 - mgf2_B2**2)) + ((mgf2_A3*lamb_d**2)/(lamb_d**2 - mgf2_B3**2))
nmgf2_d = math.sqrt(n_mgf2_d)
print('N mgf2 d=')
print(nmgf2_d)

print('\n')
# abbe number silica
abbe_number_silica = (nsilica_f - nsilica_c)/(nsilica_d - 1)
print('abbe number silica=')
print(abbe_number_silica)

print('\n')
# abbe number mgf2
abbe_number_mgf2 = (nmgf2_f - nmgf2_c)/(nmgf2_d - 1)
print('abbe number mgf2=')
print(abbe_number_mgf2)

print('\n')
#different focal ff - fc ----------------------------------------

# find focal length fd silicon to find ff-fc
fdsilica = 1/(((math.sqrt(nsilica_d)- n1)/n1)*(1/R1-1/R2))
ff_fc_silica = -fdsilica/abbe_number_silica
print('focal length ff-fc silica')
print(ff_fc_silica,"cm")

print('\n')
# find focal length fd mgf2 to find ff-fc
fdmgf2 = 1/(((math.sqrt(nmgf2_d)- n1)/n1)*(1/R1-1/R2))
ff_fc_mgf2 = -fdmgf2/abbe_number_mgf2
print('focal length ff-fc mgf2')
print(ff_fc_mgf2,"cm")

