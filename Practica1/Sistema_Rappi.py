# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 00:06:41 2022

@author: josev
"""
# Estructuras condicionales 
#if num==1 and num ==2:
    #print('el numero', num, 'cumple con la condi')
'''---------------------------------------------'''    
#if pal == 'si' or pal == yes:
        #print('se cumple con la condi')
'''------------------------------------------'''        
#a= int (input('meta un numero igual a 5'))
#if not a == 5:
        #print('A no es igual a 5 y se cumple la condiciones')
#else:
    #print ('a es igual a 5, y no se cumple la condi')


'''Practica 1, sistema consultor de dia vaciones a los que 
los trabajadores tienen derecho segun antiguedad'''


print('"Sistema de vacaiones para trabajadores de Rappi" \n')

nombre=input('Digite el nombre del colaborador: ')
clave=int(input('Digite la clave de departamento: '))

if clave==1 or clave==2 or clave==3:
    
    Años=int(input('Digite la antiguedad del trabajor en años: \n'))
    
    if clave==1:
        print('Departamento de atencion al cliente \n')
        if Años==1:
            print(nombre,' tiene derecho a 6 dias de vaciones ')
        elif Años>=2 and Años<=6:
            print(nombre,' tiene derecho a 14 dias de vaciones')
        elif Años>=7 :
            print(nombre,' tiene derecho a 20 dias de vaciones')
        else:
            print(nombre,' no tiene derecho a vaciones')
            
            
            
    elif clave==2:
        print('Departamento de logistica \n')
        if Años==1:
            print(nombre,' tiene derecho a 7 dias de vaciones')
        elif Años>=2 and Años<=6:
            print(nombre,' tiene derecho a 15 dias de vaciones')
        elif Años>=7 :
            print(nombre,' tiene derecho a 22 dias de vaciones')
        else:
            print(nombre,' no tiene derecho a vaciones')    
        
        
        
    elif clave==3:
        print('Departamento gerencial \n')
        if Años==1:
            print(nombre,' tiene derecho a 10 dias de vaciones')
        elif Años>=2 and Años<=6:
            print(nombre,' tiene derecho a 20 dias de vaciones')
        elif Años>=7 :
            print(nombre,' tiene derecho a 30 dias de vaciones')
        else:
            print(nombre,' no tiene derecho a vaciones')    
            
            
else:
    print('La clave no existe')
    print('Asegurese de colocar bien la clave')
    print('FIN')    
     
'''-----------------------------------------'''
# Num=int(input('Digite un numero '))
# Modulo= Num%2    #me devulve el residuo
# if Modulo==0:
#     print('El numero es par')
# else:
#     print('El numero es impar')

    
