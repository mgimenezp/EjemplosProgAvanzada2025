##################################################################################
#                       Funciones map, filter y reduce                           #
##################################################################################

#
# Función map()
#
# map(funcion, iterable [, iterable2]) -> TipoMap[Tipo3]
#   funcion: Tipo1 -> Tipo3 o funcion: Tipo1 x Tipo2 -> Tipo3 o etc.
#   iterable: Iterable[Tipo1]
#   iterable2: Iterable[Tipo2]
#
#
# # Función filter()
#
# filter(funcion, iterable) -> TipoFilter[Tipo1]
#   function: Tipo1 -> Bool
#   iterable: Iterable[Tipo1]
#
#
# Función reduce()
#
# reduce(funcion, iterable [,inicializador]) -> Tipo1
#   function: Tipo1 x Tipo2 -> Tipo1
#   iterable: Iterable[Tipo2]
#   inicializador: Tipo2 


#
# Ejemplo 1:
# Uso de map(): a cada elemento de la lista se le aplica x^2 = x * X.
#
lista = range(10)
def cuadrado(x): 
    return x * x
func_map = map(cuadrado, lista)
print("Ejemplo 1 - map():")
print(" ", list(lista))
print(" ", list(func_map))

#
# Ejemplo 2:
# Uso de filter(): filtra los elementos de la lista con aquellos que cumplen la condición.
#
def es_par(x):
    return x % 2 == 0
func_filter = filter(es_par, lista)
print("Ejemplo 2 - filter():")
print(" ", list(lista))
print(" ", list(func_filter))

#
# Ejemplo 3: 
# Uso de reduce(): suma todos los elementos de una lista.
#
from functools import reduce
def suma(x, y):
    return x + y
ret_reduce = reduce(suma, lista, 0)
print("Ejemplo 1 - reduce():")
print(" ", list(lista))
print(" ", ret_reduce)

#
# Ejemplo 1.1:
# El mismo ejemplo 1 (uso de función map()) pero usando expresión lambda.
# 
print("Ejemplo 1.1 - map():")
print(" ", list(lista))
print(" ", list(map(lambda x: x * x, lista)))

#
# Ejemplo 2.1:
# El mismo ejemplo 2 (uso de función filter()) pero usando expresión lambda.
#
print("Ejemplo 2.1 - filter():")
print(" ", list(lista))
print(" ", list(filter(lambda x: x % 2 == 0, lista)))

#
# Ejemplo 3.1:
# El mismo ejemplo 3 (uso de función reduce()) pero usando expresión lambda.
#
print("Ejemplo 3.1 - reduce():")
print(" ", list(lista))
print(" ", reduce(lambda x, y: x + y, lista, 0))


#
# Ejemplo 4:
# Uso de la función map(): Transforma cada elemento de una lista de caracteres en una lista de código ascii.
#
lista2 = ['H', 'O', 'L', 'A', ' ', 'm', 'u', 'n', 'd', 'o']
print("Ejemplo 4 - map():")
print(" ", lista2)
print(" ", list(map(lambda x: ord(x), lista2)))

#
# Ejemplo 5:
# Uso de la función filter(): Filtra los caracteres que están en minuscula.
#
lista2 = ['H', 'O', 'L', 'A', ' ', 'm', 'u', 'n', 'd', 'o']
print("Ejemplo 5 - filter():")
print(" ", lista2)
print(" ", list(filter(lambda x: x.islower(), lista2)))

#
# Ejemplo 6:
# Uso de la función reduce(): Concatena los elementos de una lista de carateres.
#
print("Ejemplo 6 - reduce():")
print(" ", lista2)
print(" ", reduce(lambda x, y: x + y, lista2, ""))

#
# Ejemplo 7:
# Uso de la función map(): Transforma cada elemento de dos lista: una de enteros y otra de caracteres (que son números) 
#  los suma y crea otra lista.
#
lista3 = [1, 2, 3, 4]
lista4 = ['5', '6', '7', '8']
print("Ejemplo 7 - map():")
print(" ", lista3)
print(" ", lista4)
print(" ", list(map(lambda x, y: x + ord(y) - ord('0'), lista3, lista4)))

