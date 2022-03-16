# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 21:16:19 2022

@author: josev
"""

#Ejemplo uno acceso a listas


# flowerList=['Rose','Lily','Tuli']

# firstElement=flowerList[0]
# print('firtsElement')
# lasttwoElements=flowerList[1:3]
# print(lasttwoElements)
# # firstElement=flowerList[0]


#Ejemplo de diccionaries

'''Recordemos que van separados por dos puntos'''
# #{Keys:Values} 

# datos={'Name':'James','Age':'20','Country':'CR'}

# for key in datos: # podemos usar de variable [key]
#     print(datos[key])



    
#Ejemplo 4, Tuplas

# dato=('Rose','Lily','Tulip')    
# for i in dato:
#     print(i)

#Ejemplo 5

'''Si necesitamos definir funciones podemos usar la funcion definida
"def"'''

# def suma(x,y):
#     sum= x+y
#     return sum
    
# result=suma(4,7)
# print(result)

'''Tambien podemos retornar mas de un valor de una funcion'''
#Por ejemplo

def Incrementoporuno(x,y):
    x=x+1
    y=y+1
    return x,y
    
num1,num2= Incrementoporuno(5,7)
print(num1)
print(num2)

              
    







