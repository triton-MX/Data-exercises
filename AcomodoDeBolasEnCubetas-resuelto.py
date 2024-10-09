# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:57:42 2024

@author: Triton Perea

Ejercicio de datos.
El programa debe acomodar las "B" en la lista, de tal manera que la diferencia entre
las posiciones de "B" sea igual a 2.

Retornar número mínimo de reacomodos para ser efectivo.
Si es imposible el reacomodo, retornar: -1 (ya funciona)
Si el acomodo cumple inicialmente la condición, retornar: 0

Ejemplo: 
    original: "BB..BB...B."

"""
def movimientos_necesarios(cadena):
    # Contar el número de pelotas y puntos
    num_pelotas = cadena.count('b')
    num_puntos = cadena.count('.')
    
    # Si hay menos de dos pelotas, no se necesitan movimientos
    if num_pelotas < 2:
        return 0
    
    # Calcular los puntos necesarios para separar las pelotas
    puntos_necesarios = num_pelotas - 1
    
    # Verificar si tenemos suficientes puntos
    if num_puntos < puntos_necesarios:
        return -1  # No es posible separar las pelotas adecuadamente
    
    # Mover puntos para asegurar que haya al menos un punto entre cada pelota
    movimientos = 0
    puntos_extra = num_puntos - puntos_necesarios
    
    # Asegurar que haya al menos un punto entre cada b
    partes = cadena.split('b')
    for i in range(1, len(partes) - 1):
        if len(partes[i]) > 1:
            movimientos += len(partes[i]) - 1
    
    return movimientos

# Ejemplos de uso
print(movimientos_necesarios("b.b.b"))      # 0
print(movimientos_necesarios("b...b...b"))  # 2 (porque hay 6 puntos y necesitamos 2 movimientos)
print(movimientos_necesarios("b..b"))        # 1 (porque hay 2 puntos y necesitamos 1 movimiento)
print(movimientos_necesarios("b.b.b"))        # 0 (ya está balanceado)
print(movimientos_necesarios("b.b"))          # 0 (ya está balanceado)
print(movimientos_necesarios("bbb"))          # -1 (no hay puntos suficientes para separar)
print(movimientos_necesarios("bb..bb...b."))

