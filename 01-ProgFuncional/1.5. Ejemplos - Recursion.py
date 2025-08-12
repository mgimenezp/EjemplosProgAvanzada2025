##################################################################################
#                       Recursión y Recursión de cola                            #
##################################################################################

#
# Ejemplo 1:
# Función que calcula el factorial de un número, usando recursión.
#
def factorial_rec(n):
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)
print("Ejemplo 1 - factorial recursivo:")
n = 10
print(f" Factorial de {n} =", factorial_rec(n))

#
# Ejemplo 2:
# Función que calcula el factorial de un número, versión imperativa.
#
def factorial_imp(n):
    producto = 1
    while n > 1:
        producto *= n
        n -= 1
    return producto
print("Ejemplo 2 - factorial imperativo:")
n = 10
print(f" Factorial de {n} =", factorial_imp(n))

#
# Ejemplo 3:
# Función que calcula el factorial de un número, usando función reduce().
#
from functools import reduce
def factorial_fos(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)
print("Ejemplo 3 - factorial imperativo:")
n = 10
print(f" Factorial de {n} =", factorial_fos(n))

#
# Ejemplo 4:
# Función que calcula el factorial de un número, usando recursión de cola.
#
def factorial_rec_cola(n, acumulador = 1):
    if n == 0:
        return acumulador
    return factorial_rec_cola(n - 1, n * acumulador)
print("Ejemplo 4 - factorial recursivo de cola:")
n = 10
print(f" Factorial de {n} =", factorial_rec_cola(n))

