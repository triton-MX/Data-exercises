# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:08:29 2024

@author: Triton Perea

Ejercicio de ordenamiento de paréntesis.
Programa que verifica si una secuencia de paréntesis está correctamente balanceada y bien formada.
Además cuenta la cantidad de movimientos necesarios para el acomodo. 

Problema de orden: O(n)

Para que una secuencia de paréntesis esté balanceada:

Cada paréntesis de apertura debe tener un paréntesis de cierre correspondiente.
Por lo tanto, el número total de paréntesis de apertura debe ser igual al número total de paréntesis de cierre.
Si el número total de paréntesis es impar, es imposible que cada paréntesis de apertura tenga un par correspondiente de cierre, y viceversa.

"""
def contar_movimientos(s):
    
    # Verificar si el número total de paréntesis es impar
    if len(s) % 2 !=0:
        return -1
    
    # Verificar si hay igual parentesis de apertura y de cierre
    n_apertura = s.count('(')
    n_cierre = s.count(')')
    if n_apertura != n_cierre:
        return -1
    
    apertura_no_balanceada = 0
    cierre_no_balanceada = 0
        
    for char in s:
        if char == '(':    
            apertura_no_balanceada += 1
        elif char == ')':
            if apertura_no_balanceada > 0:
                apertura_no_balanceada -= 1
            """
            else:
                cierre_no_balanceada += 1"""
    
    # El número total de movimientos necesarios es la suma de los paréntesis no balanceados
    movimientos = apertura_no_balanceada + cierre_no_balanceada
    return movimientos

# Ejemplos de uso
print(contar_movimientos("()"))      # 0
print(contar_movimientos("(())"))    # 0
print(contar_movimientos("(()())"))  # 0
print(contar_movimientos("()))((()"))       # 1 (se necesita un paréntesis de cierre)
print(contar_movimientos("())("))    # 2 (se necesita un paréntesis de apertura y un paréntesis de cierre)
print(contar_movimientos(")("))      # 2 (se necesita un paréntesis de apertura y un paréntesis de cierre)
print(contar_movimientos("()()("))   # 1 (se necesita un paréntesis de cierre)