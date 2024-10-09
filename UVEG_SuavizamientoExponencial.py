# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:30:50 2024

@author: Triton Perea

Programa que usa el método de la suavización exponencial para pronosticar un
un valor a partir de una tupla de datos. 

El método de suavización exponencial estima un pronóstico para cada periodo.
Por ello, se crea un dataframe del mismo tamaño que el banco de datos y para cada
periodo se estima el pronóstico, dependiendo del valor real (bancoDatos), el 
pronóstico siguiente se ajusta. 

Ecuación a usar (Arias,2020): 
    
    Pronostico_actual = Pronostico_anterior + alpha(ValorReal_anteior-Pronostico_anterior)

"""
# Librerías
import pandas as pd   #pandas para manejo de datos
import numpy as np
import math           #pyplot para graficar
from matplotlib import pyplot as plt

# Asignar la ruta absoluta del archivo csv a un objeto tipo string
rutaCSV=r"C:\...\bancoDatos.csv"

# Con el método read_csv leer el archivo y asignarlo a la variable "bancoDatos"
bancoDatos = pd.read_csv(rutaCSV, index_col=0 )

# Determinar la cantidad de columnas del dataframe
n= len(bancoDatos.columns)

# Coeficiente de amortiguamiento
alpha = 2/(n+1)     # Es un valor aproximado (Betancourt, 2016)

# Crear un dataframe del mismo tamaño y tipo que bancoDatos
pronosticos= bancoDatos.copy()

# Iniciamos un ciclo for para recorrer cada tupla (fila) de la tabla.
for i,j in enumerate(bancoDatos.index):
    
    """ Ante la falta de información, tomo la tendencia de los dos primeros
        valores, de cada fila, para estimar un primer pronóstico.
        
        beta= Valor_2016 / Valor_2015
        
        0 < beta =< 1
    """
    beta= bancoDatos.iat[i,1]/bancoDatos.iat[i,0]   # Determinar beta
    
    pronosticos.iat[i,0]= bancoDatos.iat[i,0]*beta  # Determinar primer pronóstico
    
    # Ciclo for para recorrer una por una las celdas de la fila
    for k in range(1,n):
        
        # Pronostico_actual = Pronostico_anterior + alpha(ValorReal_anteior-Pronostico_anterior)
        pronosticos.iat[i,k]= (pronosticos.iat[i,k-1] + (alpha*(bancoDatos.iat[i,k-1]-pronosticos.iat[i,k-1])))
        pass
    pass
# Imprimir en la consola los dos dataframe
print(bancoDatos)
print(pronosticos)

""" ------- Graficar -------------
 Para mejor visualización al ojo humano, el proceso de las gráficas será a continuación

 El método es recorrer la longitud del index para automatizar el proceso.
"""
for i,j in enumerate(bancoDatos.index):
    
    plt.xlabel('Año')                   # Titulo de eje horizontal
    plt.ylabel('Proporción')            # Titulo de eje vertical
    plt.title(bancoDatos.index[i])      # Titulo del gráfico
    plt.plot(bancoDatos.iloc[i], label='Valor real')    # Datos línea 1
    plt.plot(pronosticos.iloc[i], label='Pronóstico')   # Datos línea 2
    plt.legend()        # Indicar que se imprima la leyenda
    plt.grid()          # Indicar que se muestre la cuadrícula
    plt.show()          # Mostrar gráfico
    
    pass
