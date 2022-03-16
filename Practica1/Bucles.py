# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 19:18:31 2022

@author: josev
"""
#Ejemplo 1

# x=0
# while x<10:
#     print('Quirico')
#     x+=1
# print('A tope')

#Ejemplo 2 Fibonacci

# y,x=0,1
# while x<=1597: #no afecta si la condi es para 'x' y 'y'
#     print(y,x, end= " ")
#     '''Para que se cumpla que el numero siguiente es la suma de los dos
#      anteriores'''
#     y=y+x # gurado el nuevo valor en y
#     x=y+x #Luego vuelvo a guardar el valor pero en x
# print('stop')

#Ejemplo 3 sentencia breack

# print('While con la sentencia break \n')
# contador=0
# while contador <10:
#     contador +=1
#     if contador == 5:
#         break 
#     print('valor actual de la variable: ',contador)
# print('Fin del programa \n')

# #Ejemplo 3 sentencia continue

# print('\nWhile con la sentencia continue \n')
# contador=0
# while contador <10:
#     contador +=1
#     if contador == 5:
#         continue    #Basicamente me esta omitiendo el 5
#     print('valor actual de la variable: ',contador)
# print('Fin del programa')


#Ejemplo 4

#Como usar el ciclo for

#for i in ['a','b','c','d']: #el elemento a recorrer puede ser lo que sea
# for i in [1,2,3,4]:# puede ser una lista,tupla,cadena,rangos
#     print('Hola soy German')
    
# for e in 'hola': 
#     print("1", end=",")
 


#Ejemplo 5
   
# email=False
# while email!=True: #Esto es para que lo vuelva a pedir hasta que sea correcto
#     correo=input('Correo: ')
#     for i in correo: 
#         if i=='@':
#             email=True     
#     if email==True: #tambien puedo colocar solo 'email' que por default me lo coloca como true
#         print('el email es correcto')
#     else:
#         print('El email no es correcto')
        
        
        
#Ejemplo 6
#Pero si quiero hacer dos comparaciones necesito un contador
 
email=False

while email!=True: #Esto es para que lo vuelva a pedir hasta que sea correcto

    correo=input('Correo: ')
    contador=0
    for i in correo: 
        if i=='@': 
            contador=contador+1
    for e in correo:
        if e=='.':
            contador=contador+1
    if contador==2:
        email==True
        print('el email es correcto')
    else:
        print('El email no es correcto')
        