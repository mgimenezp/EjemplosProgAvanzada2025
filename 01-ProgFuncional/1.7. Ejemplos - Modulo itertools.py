##################################################################################
#                             Módulo itertools                                   #
##################################################################################

#
# Ejemplo 1:
# Función chain(): Iterador que se combina a partir de otros 4 iteradores.
#
from itertools import chain
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista3 = (4, 5)
rango1 = range(6, 10)
diccionario1 = {'nombre': 'Juan', 'edad': 30}
iterador_chain = chain(lista1, lista2, lista3, diccionario1, rango1)
print("Ejemplo 1 - chain():")
print(" ", lista1)
print(" ", lista2)
print(" ", lista3)
print(" ", list(rango1))
print(" ", list(iterador_chain))

#
# Ejemplo 2:
# Función permutations(): Crea un iterador que realiza las permutaciones N de N.
#
from itertools import permutations 
lista = [1, 2, 3]
iterador_permitacion_NdeN = permutations(lista)
print("Ejemplo 2 - permitacion() N de N:")
print(" ", lista)
print(" ", list(iterador_permitacion_NdeN))

#
# Ejemplo 3:
# Función permutations(): Crea un iterador que realiza las permutaciones M de N.
#
from itertools import permutations 
lista = [1, 2, 3, 4]
iterador_permitacion_MdeN = permutations(lista, 2)
print("Ejemplo 3 - permitacion() M de N:")
print(" ", lista)
print(" ", list(iterador_permitacion_MdeN))

#
# Ejemplo 4:
# Función combinations(): Crea un iterador que realiza las combinaciones N de N.
#
from itertools import combinations
elementos = ['a', 'b', 'c']
iterador_combinatoria_NdeN = combinations(elementos, 3)
print("Ejemplo 4 - combinations() N de N:")
print(" ", elementos)
print(" ", list(iterador_combinatoria_NdeN))

#
# Ejemplo 5:
# Función combinations(): Crea un iterador que realiza las combinaciones M de N.
#
cadena = "abcd"
iterador_combinatoria_MdeN = combinations(cadena, 2)
print("Ejemplo 5 - combinations() M de N:")
print(" ", cadena)
print(" ", list(iterador_combinatoria_MdeN))

#
# Ejemplo 6:
# Función tee(): Crea 2 iterador a partir de 1.
#
from itertools import tee
lista = [1, 2, 3, 4, 5]
iter1, iter2 = tee(lista, 2)
print("Ejemplo 6 - tee():")
print(" Iterador 1:", end=" ")
for item in iter1:
    print(item, end=" ")
print(" ")
print(" Iterador 2:", end=" ")
for item in iter2:
    print(item, end=" ")
print(" ")

#
# Ejemplo 7:
# Función accumulate(): Crea un iterador a partir de una lista de numeros aplicando la suma acumulativa.
#
from itertools import accumulate
numeros = [1, 2, 3, 4, 5]
suma_acumulada = list(accumulate(numeros))
print("Ejemplo 7 - accumulate() - suma:")
print(" ", suma_acumulada)

#
# Ejemplo 8:
# Función accumulate(): Crea un iterador a partir de una lista de numeros aplicando la multiplicación acumulativa.
#
producto_acumuldo = list(accumulate(numeros, lambda x, y: x * y))
print("Ejemplo 8 - accumulate() - multiplicación:")
print(" ", producto_acumuldo)
