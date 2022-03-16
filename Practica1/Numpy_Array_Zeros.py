# -*- coding: utf-8 -*-

import numpy as np

zerosArray=np.zeros(10)
print(zerosArray) ##Sin embargo, me sale un array de floats
print('\n')

#Podemos usar numpy.ndarray.astype()
#Para convertir de floats a integres
zerosArray= zerosArray.astype(int)

print(zerosArray)
print('\n')

#Para llenar el array de ones
#Usamos .ones()
onesArray=np.ones(10)
print(onesArray) ##Sin embargo, me sale un array de floats
print('\n')

#Podemos usar numpy.ndarray.astype()
#Para convertir de floats a integres
onesArray= onesArray.astype(int)

print(onesArray)
print('\n')


#Ejemplo 4
#Para usar arrays prellenados
#usamos .full()


prefulledArray=np.full(10,5) #10= tamaño del arreglo
                             #5= el valor que queremos en nuestra lista
print(prefulledArray)
print('\n')













