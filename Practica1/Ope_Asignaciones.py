# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 00:14:20 2022

@author: josev
"""
print('Calculadora con una sola variable \n')

print('Menu de opciones \n')

print('1. Suma \n'+'2. Resta \n'+'3. Multiplicacion \n'+'4. Division \n'+'5. Div Entera \n'+'6. Exponente \n'+'7. Modulo o resto \n')

Num=int(input('Introduce la opcion deseada: '))
print('\n')

if Num==1:
    print('Elegiste la suma')
    Numero=int(input('Introduce el primer numero: '))
    Numero+=int(input('Introduce el segundo numero: '))
    
    print('El resultado de la suma es: ', Numero)
    
elif Num==2:
    print('Elegiste la resta')
    Numero=int(input('Introduce el primer numero: '))
    Numero-=int(input('Introduce el segundo numero: '))
    
    print('El resultado de la resta es: ', Numero)
    
elif Num==3:
    print('Elegiste la Multiplicacion')
    Numero=int(input('Introduce el primer numero: '))
    Numero*=int(input('Introduce el segundo numero: '))
    
    print('El resultado de la multiplicacion es: ', Numero)
elif Num==4:#recordar que resivimos valores float
    print('Elegiste la Division')
    Numero=float(input('Introduce el primer numero: '))
    Numero/=float(input('Introduce el segundo numero: '))
    
    
    print('El resultado de la division es: ', round(Numero,2))#recordemos limitar los decimales
elif Num==5:
    print('Elegiste la Divi entera')
    Numero=int(input('Introduce el primer numero: '))
    Numero//=int(input('Introduce el segundo numero: '))
    
    print('El resultado de la div entera es: ', Numero)
elif Num==6:
    print('Elegiste la Exponente')
    Numero=int(input('Introduce el primer numero: '))
    Numero**=int(input('Introduce el segundo numero: '))
    
    print('El resultado del exponente es: ', Numero)
elif Num==7:
    print('Elegiste Modulo o resto')
    Numero=int(input('Introduce el primer numero: '))
    Numero%=int(input('Introduce el segundo numero: '))
    
    print('El resultado del modulo o resto es: ', Numero)
else:
    print('Seleccione un numero del menu')
