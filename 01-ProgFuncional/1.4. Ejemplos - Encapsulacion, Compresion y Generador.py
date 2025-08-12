##################################################################################
#               Encapsulación, Comprensión y Generador                           #
##################################################################################


#################
# Encapsulación #
#################

#
# Ejemplo 1:
# Rutina que duplica los valores de una lista sin encapsular.
#
# Se genera la colección
coleccion = []
for elem in range(1,10):
    coleccion.append(elem * 2)
# Se procesa la colección
print("Ejemplo 1 - Sin encapsulada:")
print(" ", end="")
for elem in coleccion:
    print(elem, end=" ")
print(" ")

#
# Ejemplo 2:
# Rutina que duplica los valores de una lista encapsulando.
#
# Se define la creación de la colección
def crear_coleccion(datos):
    coleccion = []
    for elem in datos:
        coleccion.append(elem * 2)
    return coleccion
# Se procesa la colección
print("Ejemplo 2 - Encapsulada:")
print(" ", end="")
datos = range(1,10)
for elem in crear_coleccion(datos):
    print(elem, end=" ")
print(" ")


########################
# Comprensión de lista #
########################

#
# Ejemplo 3:
# Rutina que duplica el valor de una lista si es impar sino deja el mismo valor, sin comprensión.
#
datos = range(1,10)
coleccion = []
for elem in datos:
    if (elem % 2 == 0):
        coleccion.append(elem)
    else:
        coleccion.append(elem * 2)
print("Ejemplo 3 - Sin comprensión:")
print(" ", list(datos))
print(" ", coleccion)

#
# Ejemplo 4:
# Rutina que duplica el valor de una lista si es impar sino deja el mismo valor, con comprensión de lista.
# 
datos = range(1,10)
lista = [d if d % 2 == 0 else d * 2 for d in datos]
print("Ejemplo 4 - Con comprensión de lista:")
print(" ", list(datos))
print(" ", lista)


###########################################
# Comprensión de diccionarios y conjuntos #
###########################################

#
# Ejemplo 5:
# Rutina que crea un diccionario que asocia un número y la letra asociada, conciderando A = 0, de forma imperativa.
#
datos = range(9)
diccionario = dict()
for i in datos:
    diccionario[i] = chr(65+i)
print("Ejemplo 5 - Imperativo:")
print(" ", diccionario)

#
# Ejemplo 6:
# Rutina que crea un diccionario que asocia un número y la letra asociada, conciderando A = 0, usando compresión.
#
diccionario = {i:chr(65+i) for i in datos}
print("Ejemplo 6 - Comprensión:")
print(" ", diccionario)

#
# Ejemplo 7:
# Rutina que crea un conjunto con las letras a partir de un número, considerando A = 0, de forma imperativa.
#
conjunto = set()
for i in datos:
    conjunto.add(chr(65+i))
print("Ejemplo 7 - Imperativo:")
print(" ", conjunto)

#
# Ejemplo 8:
# Rutina que crea un conjunto con las letras a partir de un número, considerando A = 0, usando compresión.
#
conjunto = {chr(65+i) for i in datos}
print("Ejemplo 8 - Comprensión:")
print(" ", conjunto)


############################
# Comprensión de generador #
############################

#
# Ejemplo 9:
# Rutina que duplica el valor de una lista si es impar sino deja el mismo valor, usando comprensión de lista.
#  Usa mucha memoria.
#
datos = range(1, 100)
lista = [d if d % 2 == 0 else d * 2 for d in datos]
print("Ejemplo 9 - Con comprensión de lista:")
print(" ", lista)

#
# Ejemplo 10:
# Rutina que duplica el valor de una lista si es impar sino deja el mismo valor, usando comprensión de generador.
#  Usa poca memoria.
#
generador = (d if d % 2 == 0 else d * 2 for d in datos)
print("Ejemplo 10 - Con comprensión de generador:")
print(" ", end="")
for num in generador:
    print(num, end=" ")
print(" ")

#
# Ejemplo 11:
# Rutina que genera tuplas con el valor valor origian y el doble a partir de una lista de números, usando comprensión de generador.
#  Usa poca memoria.
#
generador_tupla = ((d, d*2) for d in datos)
print("Ejemplo 11 - Con comprensión de generador de tuplas:")
print(" ", end="")
for num1, num2 in generador_tupla:
    print(f"({num1}, {num2})", end=" ")
print(" ")

#
# Ejemplo 12:
# Generador infinito de números.
#
generador_infinito = (d for d in range(1,))
print("Ejemplo 12 - Generador infinito de números:")
print(" ", end="")
for num in generador_infinito:
    print(num, end=" ")
print(" ")

#
# Ejemplo 13:
# Transformación de cada lista de números a su cuadrado usando map().
#
datos = range(10)
transforma_map = map(lambda x: x * x, datos)
print("Ejemplo 13 - map:")
print(" ", end="")
for x in transforma_map:
    print(x, end=" ")
print(" ")

#
# Ejemplo 14:
# Transformación de cada lista de números a su cuadrado usando generador.
#
transforma_generador = (x * x for x in datos)
print("Ejemplo 14 - generador:")
print(" ", end="")
for x in list(transforma_generador):
    print(x, end=" ")
print(" ")

#
# Ejemplo 15:
# Se filtran los números pares de una lista de números usando filter().
#
filtra_filter = filter(lambda x: x % 2 == 0, datos)
print("Ejemplo 15 - filter:")
print(" ", end="")
for x in filtra_filter:
    print(x, end=" ")
print(" ")

#
# Ejemplo 16:
# Se filtran los números pares de una lista de números usando generador.
#
filtra_generador = (x for x in datos if x % 2 == 0)
print("Ejemplo 16 - generador:")
print(" ", end="")
for x in filtra_generador:
    print(x, end=" ")
print(" ")
