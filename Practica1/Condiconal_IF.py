# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 22:34:24 2022

@author: josev
"""

# #Practica -------------------------------
# '''De esta forma puedo hacer comnetarios
# multi linea, siempre con comillas triples
# no importa cuanto salte '''
# print('''Podemos usar 
#       comillas triples para respetar los
#       saltos de linea facilmente''') #sin usar  
#    #    \n para salto de linea, alt +92
   
# Palabra=input('Meta la palabra: ')
# entero=int(input('Ingrese un numero entero: '))
# Flotante=float(input('Ingrese un numero flotante: '))
# Complejos=complex(input('Ingrese un numero complejo: '))

# print('string: ', Palabra)
# print('entero: ',entero)
# print('flotante: ',Flotante)
# print('complejo: ',Complejos)

#----------------------Fin de programa 1-----------------------------

# #----------------------Inicio de programa 2-----------------------------
# print('Sistema para el calculo de notas')
# Nota_pasa=7
# nombre=input('Ingrese el nombre de estudiente: ')
# Nota_mate=round(float(input('Cual es su calificacion en mate: ')))
# Nota_quimica=round(float(input('Cual es su calificacion en Quimica: ')))
# Nota_Biolo=round(float(input('Cual es su calificacion en biologia: ')))

# #para el caso de cada materia----------------
# # if Nota_mate>=Nota_pasa  :
# #     print(nombre +' '+'Usted ha aprobado mate')
# # else : 
# #     print(nombre +' '+'Usted a reprodabo mate')
# # if Nota_quimica>=Nota_pasa  :
# #     print(nombre + ' ' 'Usted ha aprobado quimica')
# # else : 
# #     print(nombre +' '+'Usted a reprodabo quimica')
# # if Nota_Biolo>=Nota_pasa  :
# #     print(nombre +' '+'Usted ha aprobado biologia')
# # else : 
# #     print(nombre + ' '+'Usted a reprodabo bilogia')

# # para el caso de que solo valga el promedio

# promedio=(Nota_mate+Nota_quimica+Nota_Biolo)/3

# if promedio>=Nota_pasa:
#     print('Felicidades'+' '+nombre+'  "Aprovaste" '+ 'con un promedio de: ',"{:.2f}".format(promedio))
    
# else:
#     print('Lo lamento'+' '+nombre+'  "Reprovaste" '+ 'con un promedio de: ', round(promedio,4))

# print('fin')
#  #------------------------------Fin de programa--------------   

#--------------Inicio de programa------------


print('Menu de opciones: \n')

print('Digite 1 si quiere convertir de numero a palabra: ')
print('Digite 2 si quiere convertir de palabra anumero: ')

opcion=int(input('Cual es tu opcion deseada?:'))



if opcion==1:
    print('Conversor de numero a palabra \n')
    Num_covertir=int(input('Digite el numero que desea convertir a palbra?:'))
    if Num_covertir==1:
        print('el numero es: '+'"UNO"')
    elif Num_covertir==2:
        print('el numero es: '+'"DOS"')
    elif Num_covertir==3:
        print('el numero es: '+'"TRES"')
    elif Num_covertir==4:
        print('el numero es: '+'"CUATRO"')
    else:
        print('El numer no se encuentra disponible')
    
elif opcion==2:
    print('Conversor de palabra a numero \n')
    Pal_covertir=input('Digite la palabra que desea convertir a numero?:')
    
    Pal_covertir=Pal_covertir.lower()#Para que acepte: CUatro o cuatro o CUATRO
    
    

    if Pal_covertir=="UNO":
        print('el numero es: '+'"1"')
    elif Num_covertir=='DOS':
        print('el numero es: '+'"2"')
    elif Num_covertir=='TRES':
        print('el numero es: '+'"3"')
    elif Num_covertir=='CUATRO':
            print('el numero es: '+'"4"')

else:
    print('Opcion no disponible, reintente de nuevo')
     



    
