# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 23:21:51 2022

@author: josev
"""
print('Cual es el numero mas grande de los 3')


Num_1=int(input('Digite el primer numero:'))
Num_2=int(input('Digite el segundo numero:'))
Num_3=int(input('Digite el tercer numero:'))

if Num_1>Num_2 and Num_1>Num_3:
    print('El numero mayor de los tres es: ',Num_1)
elif Num_2>Num_1 and Num_2>Num_3:
    print('El numero mayor de los tres es: ',Num_2)
else:
    print('El numero mayor de los tres es: ',Num_3)
    
    
#else:
     # if Num_2>Num_3:
     #     print('el numero 2 es el mas grande')
     # else:
     #     print('el numero 3 es el mas grande')
    