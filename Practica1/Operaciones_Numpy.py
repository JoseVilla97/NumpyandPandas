# -*- coding: utf-8 -*-
import numpy as np

#Addicion (+)

matrix=np.array([[1,2,3],[4,5,6]])
print(matrix)

print('\n')

print(matrix + 2)#se suma a cada elemento del array

'''Lo anterior no se puede hacer con una lista normal'''
print('\n')
#Sustraction

print(matrix - 2)

print('\n')

#Multiplicattion
print(matrix * 2)

print('\n')

#Division
print(matrix / 2)#Division normal
print(matrix // 2)#Division entera

print('\n')

#Raise to a power
print(matrix ** 2)

print('\n')

#Transpose
print(matrix.T)

print('\n')

#sumar cada elemento de un array con cada de otro array
matrix1=np.array([[1,2,3],[4,5,6]])
print(matrix1)
matrix2=np.array([[-1,-2,-3],[-4,-5,-6]])
print(matrix2)
print(matrix1 + matrix2)

'''Si hago lo anterior con array normales, lo que voy hacer es concatenar'''
print('\n')



#sumar cada elemento de un array con cada de otro array
print(matrix1 - matrix2)
print('\n')

#Multiplicacion
print(matrix1 * matrix2) 


print('\n')
print(matrix1 / matrix2)
print('\n')
print(matrix1 // matrix2)
print('\n')


a=np.array([ [1,2,3],[4,5,6],[0,0,0] ])
b=np.array([ [-1,-2,-3],[-4,-5,-6],[0,0,0,] ])
#Podemos usar matmull() para hacer l
c=np.matmul(a,b)
print(c)

print('\n')


#Stadistic-------------------------------------------------------------------
MM=np.array([[1,2,3],[4,5,6]])
#Para encontrar el minimo de toda la matriz
minimo=np.min(MM)
print(minimo)

print('\n')
maximo=np.max(MM)
print(maximo)
print('\n')
suma=np.sum(MM)
print(suma)
print('\n')


promedio=np.mean(MM)
print(promedio)
print('\n')

#Division estandar

std=np.std(MM)
print(std)
print('\n')

mediana=np.median(MM)
print(mediana)
print('\n')





















