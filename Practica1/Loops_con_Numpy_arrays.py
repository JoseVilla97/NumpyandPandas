# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 22:30:17 2022

@author: josev
"""
import numpy as np

# oneArray=[1,2,3,4,5]
# for i in oneArray: #Me recorre todo el arreglo 
#     print(i)



 #  '''En una dimension''' 
two1Array=np.array([[1,2,3],[4,5,6]])
for i in two1Array: #Me recorre todo el arreglo 
    print(i)
print('\n')
#   '''En dos dimensiones'''
two2Array=np.array([[1,2,3],[4,5,6]])
for i in two2Array: #Recorre cada 2D, osea despliega los grupos de 2D
    for j in i:#Recorre pero en 1D, osea todos los numeros del array
        print(j)
print('\n')
#       '''En 3 dimensiones''' 
threArray=np.array([[[1,2,3],[-1,-2,-3]],[[4,5,6],[-4,-5,-6]]])

for i in threArray: #Me depliega paquetes en 2D

    for j in i:#Me depliega paquetes en 1D
    
        for k in j:# Me despliega los elementos del arreglo
            
            print(k)