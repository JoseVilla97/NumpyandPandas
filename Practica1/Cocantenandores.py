# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 14:32:47 2022

@author: josev
"""

#Ejemplo de concatenación

# nombre = 'jose'
# edad=20
 
 
# print('Hola {} tienes {} anios'.format(nombre,edad))

# print('Hola {0} tienes {1} anios'.format(nombre,edad))#segun posici[on]

# print('Hola {nombre} tienes {edad} anios'.format(nombre='jose',edad=20))


#Usando el f"strings"

# print(f"Hola {nombre} tienes {edad}")


#Ejemlpos para cortar cadenas

#cadena.strip("Caracteres que quiero que se eliminen")
'''recordemos que se debe indicar so es mayucula o minuscula'''

cadena= ' Hola Ernesto '# con espacios
cadena=cadena.strip("s tHo")

print(cadena)#-------la Erne
