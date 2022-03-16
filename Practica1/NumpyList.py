# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 00:44:04 2022

@author: josev
"""


import numpy as np

# print('EJEMPLO 1')
# oneDarray=np.array([1,2,3,4,5])
# print(oneDarray)
# #Si queremos ver algunas características del arreglo 


# print(oneDarray.ndim) # ndim para indicar la dimensiones
# print(oneDarray.shape) #5X1

# largo=len(oneDarray) # elementos en la primera dimension
# print(largo)

'''Creación de arreglos de 2 y 3 dimensiones.'''

# print('\nEJEMPLO 2\n')
# twoDarray=np.array([[1,2,3],[4,5,6]])#ver orden de las comas

# print(twoDarray)
# print(twoDarray.ndim) # ndim para indicar la dimensiones


# print('\nEJEMPLO 3\n')

# #-------------------[  '''[ [],[] ],'''' [ [],[] ]''' ]
# threDarray=np.array([[[1,2,3],[-1,-2,-3]],[[4,5,6],[-4,-5,-6]]])#ver orden de las comas

# #---------------------[2D--+--2D]

# print(threDarray)
# print(threDarray.ndim) 


# '''Esto tambien es 3D por los square brackets '''
# sDarray=np.array([[[1,2,3,4,5]]])
# print(sDarray.ndim) 


threeeDarray=np.array([[[1,2,3],[-1,-2,-3]],[[4,5,6],[-4,-5,-6]]])#ver orden de las comas

print(threeeDarray [0],'\n')#Toma el 2D
print('\n',threeeDarray [0,0],'\n')#Toma el 1D
print('\n',threeeDarray [0,0,0])#Toma el valor de la cadena



two2Darray=np.array([[1,2,3],[4,5,6]])

print(two2Darray.shape)
'''Esto me despliga (2,3)
            2=las dimensiones
            3=es el de elemento en el array'''
            





















