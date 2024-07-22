#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Codificaciones posibles: iso-8859-15, utf-8
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import os
from directorios import *

#####
def leerDirectorio(direccion, formato='raw'):
    '''Detecta automáticamente los archivos según el 'formato' especificado.
    Devuelve una lista con el nombre de los archivos y otra con la dirección
    completa al archivo.
    PRE: El formato debe tener tres caracteres luego del punto final'''
    archivos = os.listdir(direccion)
    #Filtrado
    if formato:
        archivos = [e for e in archivos if e[-3:] == formato]
    direcciones = [a+b for a,b in zip([direccion]*len(archivos),archivos)]
    return archivos, direcciones
#####
def graficar(a, etiqueta = '', columnas = [3, 2], y_unidades = None):
    '''Grafica Esfuerzo de tracción vs Deformación.
    Si truncar=True, omite en el gráfico el régimen de descarga o baja de la
    tensión por falla al final del ensayo.
    Etiqueta permite añadir una leyenda a la curva. Útil para ciclos.'''
    x = a[a.columns[columnas[0]]] #Temperatura
    y = a[a.columns[columnas[1]]] #Cambio en longitud

    plt.plot(x, y, linewidth=2, label = etiqueta)
    
    if etiqueta: plt.legend()
    plt.xlabel('Temperatura [$^{\circ}$C]')
    if y_unidades: plt.ylabel(f'Cambio en longitud, $\Delta$L [{y_unidades}]')
    else: plt.ylabel('Cambio en longitud, $\Delta$L [$\mu$m]')
    plt.grid(True)
    #plt.xticks() #agregar ticks menores
    plt.show()
#####
#####
#####
#####
#####

#%% DILATOMETRIAS CAC
archivos, direcciones = leerDirectorio(directorio_dil, formato = 'dat')

#Separador = \t , saltear columnas = 0 , formato = utf-8
separador = '\t'
saltear_filas = None
decimal = ','
separador_mil = None
codificacion = None

a = [(etiqueta.split('.')[0],
      pd.read_csv(archivo, sep = separador, skiprows = saltear_filas,
                  encoding = codificacion, decimal = decimal,
                  thousands = separador_mil))
     for etiqueta, archivo in zip(archivos, direcciones)]
#%%

for e in a: graficar(e[1], etiqueta = e[0])

for i,e in enumerate(a): print(f'[{i}]',e[0])
indice = [3]
for i in indice: graficar(a[i][1], columnas = [3, 2], etiqueta = a[i][0])


####################################
#%% DILATOMETRIAS CINI

archivos, direcciones = leerDirectorio(directorio_cini, formato = None)

nomenclatura = {'d01': '10', 'd02':'20', 'd03':'40', 'd04':'60', 'd05':'80', 'd06':'10', 'd07':'50', 'd08':'30'}

'''nomenclatura
d01 10
d02 20
d03 40
d04 60
d05 80
d06 10
d07 50
d08 30'''

#Separador = \t , saltear columnas = 0 , formato = utf-8
separador = '\t'
saltear_filas = None
decimal = '.'
separador_mil = None
codificacion = None

b = [(etiqueta.split('.')[1], pd.read_csv(archivo, sep = separador, skiprows = saltear_filas, encoding = codificacion, decimal = decimal, thousands = separador_mil)) for etiqueta, archivo in zip(archivos, direcciones)]

b = [(nomenclatura[e[0]], e[1]) for e in b]
b

#%%
for e in b: graficar(e[1], columnas = [4, 1], etiqueta = e[0], y_unidades = 'mm')

for i,e in enumerate(b): print(f'[{i}]',e[0])
indice = [3]
for i in indice: graficar(b[i][1], columnas = [4, 1], etiqueta = b[i][0], y_unidades = 'mm')

####################################
#%% DILATOMETRIAS MLC TESINA (CINI)
archivos, direcciones = leerDirectorio(directorio_mlc, formato = '')

#Separador = \t , saltear columnas = 0 , formato = utf-8
separador = '\t'
saltear_filas = None
decimal = '.'
separador_mil = None
codificacion = None

c = [(etiqueta.split('.')[1], pd.read_csv(archivo, sep = separador, skiprows = saltear_filas, encoding = codificacion, decimal = decimal, thousands = separador_mil)) for etiqueta, archivo in zip(archivos, direcciones)]
#%%

for e in c: graficar(e[1], columnas = [3, 1], etiqueta = e[0], y_unidades = 'mm')

for i,e in enumerate(c): print(f'[{i}]',e[0])
indice = [1,2,3]
for i in indice: graficar(c[i][1], columnas = [4, 1], etiqueta = c[i][0], y_unidades = 'mm')




####################################
#%%

























