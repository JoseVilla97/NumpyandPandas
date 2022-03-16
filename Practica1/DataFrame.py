# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

Lista=[ ['Aple','Red'],['Banana','Yellow'],['Orange','Orange'] ]

MarcoDatos=pd.DataFrame(Lista)

#Para nombrar las columnas
MarcoDatos=pd.DataFrame(Lista,columns=['Fruits','Colors'])
print(MarcoDatos)

print('\n')

#Por otro lado-------------------------------------------------------------
#Podemos crear Datframe con uso de librearias
# Nom_Colum: [Lo que va en cada fila]
myDictianary={'Fruits':['Aple','Bananna','Orange'],'Color':['Red','Yellow','Orange']}
MarcoDatos2=pd.DataFrame(myDictianary)
print(MarcoDatos2)


#---------------------------------------------------------------
#Podemos cargar files csv como un DataFrame desde nuestro dispositivo
'''df=pd.read_csv('cereales.csv')
 print(df)'''