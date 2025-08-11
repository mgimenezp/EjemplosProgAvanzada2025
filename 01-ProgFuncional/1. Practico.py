##################################################################################
#                                 Practico 1                                     #
##################################################################################


#################################################
#             Map, filter y reduce              #
#################################################
    
#
# Ejercicio 1:
# Crear una función, con nombre calcula_iva_lista, que tome una lista de precios y devuelva un lista con el calculo del iva. 
#
def calcula_iva(precio):
    return precio * 0.22
def calcula_iva_lista(lista):
    return list(map(calcula_iva, lista))     # return list(map(lambda x: x * 0.22, lista))
lista = [10, 25.5, 50, 15, 45.3, 100, 5, 82.8]
print("Ejercicio 1:")
print(" Lista de precios:", lista)
print(" Lista de IVAs:", calcula_iva_lista(lista))

#
# Ejercicio 2:
# Crear una función, con nombre precios_mayores, que tome una lista de precios y un precio y 
#  devuelva un lista con los precios mayores o iguales al precio ingresado. 
#
def precios_mayores(lista, precio):
    return list(filter(lambda x: x>= precio, lista))
precio = 30
print("Ejercicio 2:")
print(" Lista de precios:", lista)
print(f" Lista de precios mayores a {precio}: ", precios_mayores(lista, precio))

#
# Ejercicio 3:
# Crear una función, con nombre suma_precios_con_iva, que tome una lista de precios sin iva y 
#  devuelva un valor con la suma de los precios con iva. 
#
from functools import reduce
def acumula_precio_con_iva(acumulador, precio):
    return acumulador + calcula_iva(precio) + precio
def suma_precios_iva_lista(lista):
    return reduce(acumula_precio_con_iva, lista, 0)              # return reduce(lambda x, y: x + y * 1.22, lista, 0)
print("Ejercicio 3:")
print(" Lista de precios:", lista)
print(" Suma de precios con iva: ", suma_precios_iva_lista(lista))

#
# Ejercicio 4:
# Crear una función, con nombre precio_a_pagar, que tome una lista de productos de un carrito con precios y 
#  porcentaje de descuento y devuelva la suma a pagar aplicando el descuento e iva a cada producto.  
#
def precio_a_pagar(carrito):
    def precio_de_producto(producto):
        precio_con_descuento = producto[0] * ((100 - producto[1]) / 100)
        return precio_con_descuento + calcula_iva(precio_con_descuento)
    return reduce(lambda x, y: x + y, map(precio_de_producto, carrito))
carrito = [(50, 5), (220, 15), (40, 0), (590, 25), (120, 0), (350, 10)]
print("Ejercicio 4:")
print(" La lista de productos es: ", carrito)
print(" El precio a pagar es: ", precio_a_pagar(carrito))

#
# Ejercicio 5:
# Crear una función, con nombre empieza_mayuscula_palabras, que reciba una frase y 
#  devuelva la frase pero con todas sus palabras empezando en mayuscula. 
#
def empieza_mayuscula_palabras(frase):
    palabras = frase.split()
    return reduce(lambda x, y: x + " " + y, map(lambda palabra: palabra[0].capitalize() + palabra[1:], palabras))
frase = "Aprendiendo programación funcional en Python"
print("Ejercicio 5:")
print(" Frase original:", frase)
print(" Frase modificada:", empieza_mayuscula_palabras(frase))

#
# Ejercicio 6:
# Crear una función, con nombre extraer_digitos, que reciba una lista de string y 
#  devuelva una lista con los mismos string quitando los dígitos. 
#
def extraer_digitos(palabras):
    def extraer_digitos_palabra(palabra):
        return reduce(lambda x, y: x + y, filter(lambda caracter: not caracter.isdigit(), palabra))
    return list(map(extraer_digitos_palabra, palabras))
palabras = ["Apr8endi70endo1", "0prog345ramaci7ón", "fun4cion6al9", "en", "1Pyth5on1"]
print("Ejercicio 6:")
print(" Lista de palabras originales:", palabras)
print(" Lista de palabras sin dígitos:", extraer_digitos(palabras))

#
# Ejercicio 7:
# Crear una función, con nombre eliminar_duplicados, que reciba una lista de números y 
#  devuelva una lista sin los números duplicados y en el orden original, usando reduce. 
#
def eliminar_duplicados(numeros):
    return reduce(lambda x, y: x + [y] if not y in x else x, numeros, [])
numeros = [2, 6, 4, 2, 5, 1, 2, 5, 9, 1, 0, 4]
print("Ejercicio 7:")
print(" Lista original:", numeros)
print(" Lista sin duplicados:", eliminar_duplicados(numeros))

#
# Ejercicio 8:
# Crear una función, con nombre largo_palabras, que reciba una frase y 
#  devuelva un diccionario con las palabras y su longitud.
#
def largo_palabras(frase):
    palabras = frase.split()
    return dict(map(lambda palabra: (palabra, len(palabra)), palabras))
frase = "Aprendiendo programación funcional en Python"
print("Ejercicio 8:")
print(" Frase orginal:", frase)
print(" Palabras con largos:", largo_palabras("Aprendiendo programación funcional en Python"))

#
# Ejercicio 9:
# Crear una función, con nombre cuenta_vocales_lista, que reciba una lista de strings y 
#  devuelva una lista con tuplas con el string y la cantidad de vocales que tiene. 
#
import re
def cuenta_vocales_lista(lista_textos):
    def es_vocal(caracter): 
        return bool(re.match(r"[aeiouAEIOU]", caracter))
    def cuenta_vocales(texto):
        return len(reduce(lambda x, y: x + y if es_vocal(y) else x, texto))
    return reduce(lambda x, y: x + [(y, cuenta_vocales(y))], lista_textos, [])
lista_textos = ["Estoy", "intentando", "aprender", "programación funcional", "en", "Python"]
print("Ejercicio 9:")
print(" Lista de textos originales:", lista_textos)
print(" Textos con cantidad de vocales:", cuenta_vocales_lista(lista_textos))

#
# Ejercicio 10:
# Crear una función, con suma_listas, que reciba 2 listas de números y
#  devuelva una lista con las sumas de sus elementos en la misma posición.
#
def suma_listas(lista1, lista2):
    return map(lambda x, y: x + y, lista1, lista2)
lista1 = [3, 2, 6, 8, 5]
lista2 = [1, 8, 0, 4, 3]
print("Ejercicio 10:")
print(" Lista1:", lista1)
print(" Lista2:", lista2)
print(" Suma de las listas:", list(suma_listas(lista1, lista2)))

#
# Ejercicio 11:
# Crear una función, con nombre map_con_reduce, que reciba una función de transformación y una lista de elementos y 
#  y devuelva una lista de elementos luego de aplicarle la función a cada elemento de la lista (misma funcionalidad de map)
#  pero usando solo la función reduce. 
# Mostrar el ejemplo aplicando una función que realice el cuadrado de una lista de números.
#
def map_con_reduce(funcion, lista):
    return reduce(lambda x, y: x + [funcion(y)], lista, []) 
lista = list(range(10))
funcion = lambda x: x * x
print("Ejercicio 11:")
print(" Lista original:", lista)
print(" Lista con los cuadrados:", map_con_reduce(funcion, lista))

#
# Ejemplo 12:
# Crear una función, con nombre filter_con_reduce, que reciba una función de filtro y una lista de elementos y 
#  y devuelva una lista de elementos que cumplen el filtro (misma funcionalidad de filter)
#  pero usando solo la función reduce. 
# Mostrar el ejemplo aplicando una función que filtre los números mayores a un valor dado.
#
def filter_con_reduce(funcion, lista):
    return reduce(lambda x, y: x + [y] if funcion(y) else x, lista, [])
lista = list(range(10))
funcion = lambda x: x > 5
print("Ejercicio 12:")
print(" Lista original:", lista)
print(" Lista con > 5:", filter_con_reduce(funcion, lista))


#
# Ejercicio 13:
# Crear una función, con nombre buscar_inmuebles, que reciba una lista de inmuebles y 
#  devuelva una lista de inmuebles con valor inferior al pasado por parámetro.
#  Los detalles son los siguientes:
#   Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:
#   [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, 
#    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, 
#    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, 
#    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, 
#    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
#   Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. 
#   La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con los inmuebles 
#   cuyo precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo 
#   par a cada diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las siguiente fórmula 
#   en función de la zona:
#    Zona A: precio = (metros x 1000 + habitaciones x 5000 + garaje x 15000) x (1 - antiguedad / 100)
#    Zona B: precio = (metros x 1000 + habitaciones x 5000 + garaje x 15000) x (1 - antiguedad / 100) x 1.5
#
def buscar_inmuebles(inmuebles, presupuesto):
    def filtro(inmueble):
        return inmueble['precio'] <= presupuesto
    def añadir_precio(inmueble_param):
        inmueble = inmueble_param
        precio = (inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000 + int(inmueble['garaje']) * 15000) * (1 - (2020 - inmueble['año']) / 100)
        if inmueble['zona'] == 'B':
            precio *= 1.5
        inmueble['precio'] = precio
        return inmueble
    return list(filter(filtro, map(añadir_precio, inmuebles)))
inmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
presupuesto = 100000
print("Ejercicio 13:")
print(" Lista de inmuebles:", inmuebles)
print(f" Lista de inmuebles dentro del presupuesto de {presupuesto}:", buscar_inmuebles(inmuebles, presupuesto))


#################################################
#                  Composición                  #
#################################################

#
# Ejercicio 14:
# Crear la composición de dos funciones f(g(x)):
#  Una función, con nombre precio_con_descuento, que reciba un precio y devuelva el precio con un 10% de descuento.
#  Otra función, con nombre precio_con_iva, que reciba un precio y devuelva el precio con el IVA del 22%.
#
def precio_con_descuento(precio):
    return precio - precio * 0.1
def precio_con_iva(precio): 
    return precio * 1.22
precio = 300
precio_final = precio_con_iva(precio_con_descuento(precio))
print("Ejercicio 14:")
print(" Precio base:", precio)
print(" Precio final:", precio_final)

#
# Ejercicio 15:
# Crear una función, con nombre composicion, que permita realizar la composición de varias funciones (f o g o ...)(x).
# Luego, probar la composición con las funciones precio_con_descuento y precio_con_iva.
# Finalmente, probar que si se agrega otra función, por ejemplo una que descuente 10 pesos fijo al precio hace 
#  la composición de las 3 funciones.
#
def composicion(*funciones):
    def interna(dato, funciones=funciones):
        resultado = dato
        for funcion in reversed(funciones):
            resultado = funcion(resultado)
        return resultado
    return interna
resta_10 = lambda precio: precio - 10
precio = 300
print("Ejercicio 15 - (f o g)(x):")
comp = composicion(precio_con_iva, precio_con_descuento)
print(" Precio base:", precio)
print(" Precio final:", comp(precio))
comp = composicion(resta_10, precio_con_iva, precio_con_descuento)
print("Ejercicio 15 - (f o g o h)(x):")
print(" Precio base:", precio)
print(" Precio final:", comp(precio))


#################################################
#                 Comprensiones                 #
#################################################

#
# Ejercicio 16:
# Utilizando comprensión de listas crear una función, con nombre calcula_iva_lista_comp, que realice la misma funcionalidad el ejercicio 1, 
#  es decir, tomar una lista de precios y devolver un lista con el calculo del iva. 
#
def calcula_iva_lista_comp(lista):
    return [d * 0.22 for d in lista]
lista = [10, 25.5, 50, 15, 45.3, 100, 5, 82.8]
print("Ejercicio 16:")
print(" Lista de precios:", lista)
print(" Lista de IVAs:", calcula_iva_lista_comp(lista))

#
# Ejercicio 17:
# Utilizando comprensión de listas crear una función, con nombre precios_mayores_comp, que realice la misma funcionalidad que el ejercicio 2, 
#  es decir, tomar una lista de precios y un precio y devolver un lista con los precios mayores o iguales al precio ingresado. 
#
def precios_mayores_comp(lista, precio):
    return [d for d in lista if d >= precio]
precio = 30
print("Ejercicio 17:")
print(" Lista de precios:", lista)
print(f" Lista de precios mayores a {precio}:", precios_mayores_comp(lista, precio))

#
# Ejercicio 18:
# Utilizando comprensión de generadores crear una función, con nombre suma_precios_iva_lista_comp, que realice la misma funcionalidad que el ejercicio 3, 
#  es decir, tomar una lista de precios sin iva y devuelva un valor con la suma de los precios con iva. 
#
def suma_precios_iva_lista_comp(lista):
    return sum(calcula_iva(d) + d for d in lista)
print("Ejercicio 18:")
print(" Lista de precios:", lista)
print(" Suma de precios con iva:", suma_precios_iva_lista_comp(lista))

#
# Ejercicio 19:
# Utilizando comprensión de lista crear una función, con nombre extraer_digitos_comp, que realice la misma funcionalidad que el ejercicio 6, 
#  es decir, recibir una lista de string y devolver una lista con los mismos string quitando los dígitos. 
#
def extraer_digitos_comp(palabras):
    def extraer_digitos_palabra_comp(palabra):
        return "".join([l for l in palabra if not l.isdigit()])
    return [extraer_digitos_palabra_comp(p) for p in palabras]
palabras = ["Apr8endi70endo1", "0prog345ramaci7ón", "fun4cion6al9", "en", "1Pyth5on1"]
print("Ejercicio 19:")
print(" Lista de palabras originales:", palabras)
print(" Lista de palabras sin dígitos:", extraer_digitos_comp(palabras))

#
# Ejercicio 20:
# Utilizando compresión de diccionario crear una función, con nombre largo_palabras_comp, que realice la misma funcionalidad que el ejercicio 8, 
#  es decir, recibir una frase y devolver un diccionario con las palabras y su longitud. 
#
def largo_palabras_comp(frase):
    palabras = frase.split()
    return {palabra: len(palabra) for palabra in palabras }
frase = "Aprendiendo programación funcional en Python"
print("Ejercicio 8:")
print(" Frase orginal:", frase)
print(" Palabras con largos:", largo_palabras_comp("Aprendiendo programación funcional en Python"))

#
# Ejercicio 21:
# Usando compresión de diccionario crear una función, con nombre crear_diccionario, que reciba dos lista, una con claves y otra con valores y 
#  devuelva una diccionario que asocia las claves con los valores. Recomendación: uso de función zip(). 
#
def crear_diccionario(claves, valores):
    return {clave: valor for clave, valor in zip(claves, valores)}
claves = ['nombre', 'edad', 'ciudad', 'pais', 'profesion']
valores = ['Juan', '31', 'Montevideo', 'Uruguay', 'ingeniero']
print("Ejercicio 21:")
print(" Lista de claves:", claves)
print(" Lista de valores:", valores)
print(" Diccionario:", crear_diccionario(claves, valores))


#################################################
#                   Recursión                   #
#################################################

#
# Ejercicio 22:
# Crear una función, con nombre fibonacci, que realice el calculo de fibonacci, usando recursión.
# Matemáticamente se define: F(0) = 0, F(1) = 1, y F(n) = F(n-1) + F(n-2) para n ≥ 2.
#
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("Ejercicio 22:")
n = 10
print(f" Fibonacci de {n} =", fibonacci(n))

#
# Ejercicio 23:
# Crear una función, con nombre quicksort, que permita ordenar una lista de números aplicando el método de ordenamiento quicksort,
#  usando recursión.
def quicksort(lista):
    if len(lista) == 0:
        return lista
    pivote = lista[0]
    pivotes = [x for x in lista if x == pivote]
    menores = quicksort([x for x in lista if x < pivote])
    mayores = quicksort([x for x in lista if x > pivote])
    return menores + pivotes + mayores
numeros = [9, 1, 0, 12, 50, 3, 6, 4, 40, 23, 2, 9, 0, 12, 6]
print("Ejercicio 23:")
print(" Lista sin orden:", numeros)
print(" Lista ordenada:", quicksort(numeros))

#
# Ejercicio 24:
# Crear una función, con nombre fibonacci_rec_cola, que realice el calculo de fibonacci, usando recursión de cola.
#
def fibonacci_rec_cola(n, a = 0, b = 1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci_rec_cola(n - 1, b, a + b)
print("Ejercicio 24:")
n = 10
print(f" Fibonacci de {n} =", fibonacci_rec_cola(n))


#################################################
#       Evaluación perezosa, iteradores         #
#################################################

#
# Ejercicio 25:
# Crear una función, con nombre divisible_por, que tome un número divisor y otro número con la cantidad de valores a devolver. 
#  Devolverá una lista con los primeros valores cantidad valores divisibles, con evaluación perezosa usando comprensión de generadores.
#  Se puede simular el infinito usando un número grande en range(). Explore diferentes maneras de lograr lo solicitado.
#
def divisible_por(divisor, cantidad):
    datos = range(1,1000000)
    generador = (d for d in datos if d % divisor == 0)
    lista = []
    for _, d in zip(range(1, cantidad+1), generador):
        lista = lista + [d]
    return lista
divisor = 5
cantidad = 10
print("Ejercicio 25:")
print(f" Lista de los primeros {cantidad} números divisibles por {divisor}:", divisible_por(divisor, cantidad))

#
# Ejemplo 26:
# Crear una función, con nombre factorial_iterador_yield, que no tenga parámetros de entrada y devuelva el próximo número 
#  de la secuencia de números de factorial, con evaluación perezosa usando función generadora (sentencia yield). 
# La secuencia de números a devolver es: 1, 2, 6, etc. 
#
def factorial_iterador_yield():
    n = 1
    factorial = 1
    while True:
        factorial = factorial * n
        yield factorial
        n += 1
print("Ejercicio 26:")
n = 10
print(f" Primeros {n} números de la secuencia de factorial:", end=" ")
for _, factorial in zip(range(n+1), factorial_iterador_yield()):
    print(factorial, end=" ")
print("")

#
# Ejemplo 27:
# Crear una clase, con nombre FactorialIterador, que no tenga parámetros de entrada y devuelva el próximo número 
#  de la secuencia de números de factorial, con evaluación perezosa usando una clase como implementación de iterador. 
#
from collections.abc import Iterable
class FactorialIterador(Iterable):
    def __init__(self):
        self.n = 1
        self.factorial = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.factorial = self.factorial * self.n
        self.n += 1
        return self.factorial
factorial_iterador_clase = FactorialIterador()
print("Ejercicio 27:")
n = 10
print(f" Primeros {n} números de la secuencia de factorial:", end=" ")
for _, factorial in zip(range(n+1), factorial_iterador_clase):
    print(factorial, end=" ")
print("")

#
# Ejemplo 28:
# Crear una función, con nombre obtener_primos, que no tenga parámetros de entrada y devuelva el próximo número primo, 
#  con evaluación perezosa usando generador de funciones (sencencia yield). 
#
def obtener_primos():
    candidato = 2
    encontrados = []
    while True:
        if all(candidato % primo != 0 for primo in encontrados):
            yield candidato
            encontrados.append(candidato)
        candidato += 1
print("Ejercicio 28:")
n = 10
primos = obtener_primos()
print(f" Primeros {n} números primos:", end=" ")
primo = next(primos)
print(primo, end=" ")
for _, primo in zip(range(n+1), obtener_primos()):
    print(primo, end=" ")
print("")


#################################################
#                  Decoradores                  #
#################################################

#
# Ejercicio 29:
# Supongamos que tenemos una función, con nombre calculo_valores, que realiza una gran cantidad de calculos, por ejemplo, 
#  duplica el valor de los datos de una lista de gran tamaño.
# Queremos saber cuanto demora la ejecución de esta función, pero sin modificar el código interno.
# ¿Como se puede hacer?
# Crear la función, con nombre calculo_valores, y lo que fuese necesario para imprimir el tiempo que demora la ejecución de la función.
#
import time
def imprimir_tiempo(funcion):
    def funcion_calcula_tiempo(lista):
        inicio = time.time()
        funcion(lista)
        final = time.time()
        print(f" Tiempo de ejecución es: {final - inicio}")
    return funcion_calcula_tiempo
@imprimir_tiempo
def calculo_valores(lista):
    return list(map(lambda x: 2 * x, lista))
lista = range(5000000)
print("Ejercicio 29:")
calculo_valores(lista)

#
# Ejercicio 30:
# Crear una función, con nombre crear_lista_primeros_numeros, que cree una lista con los primeros n números pasados por parámetro.
# Necesitamos hacer que si se ejecuta esa función por segunda vez retorne la información más rápido, ¿como se puede hacer?
# Utilizar el decorador imprimir_tiempo, del ejercicio anterior, para verificar los tiempos de ejecución.
#
from functools import lru_cache
@imprimir_tiempo
@lru_cache(maxsize=32)
def crear_lista_primeros_numeros(n):
    return list(range(n))
print("Ejercicio 30:")
n1 = 1000000
n2 = 2000000
print(f" Ejecución con {n1} números:")
crear_lista_primeros_numeros(n1)
print(f" Ejecución con {n2} números:")
crear_lista_primeros_numeros(n2)
print(f" Ejecución con {n1} números nuevamente:")
crear_lista_primeros_numeros(n1)


#################################################
#               Módulo itertool                 #
#################################################

#
# Ejercicio 31:
# Crear una función, con nombre combinar_listas, que combine N listas, usando la función chain, y usando un decorador aplicar 
#  la suma a todos los elementos de la lista combinada.
#
from itertools import chain
def sumar_valores_lista(funcion):
    def funcion_sumar(*listas):
        listaCombinada = funcion(*listas)
        return reduce(lambda x, y: x + y, listaCombinada)
    return funcion_sumar
@sumar_valores_lista
def combinar_listas(*listas):
    return list(chain(*listas))
print("Ejercicio 31:")
lista1 = [1, 2, 3]
lista2 =[8, 2]
lista3 = [4, 0, 5, 9]
print(" Listas a combinar: ", lista1, lista2, lista3)
print(" Lista combinada (suma):", combinar_listas(lista1, lista2, lista3))

#
# Ejercicio 32:
# Crear una función, con nombre reparte_numeros, que reciba por parámetro la cantidad de números a repartir y la cantidad de personas,
#  y devuelva una lista con todas las posibilidades, usando el módulo itertools.
#
from itertools import permutations
def reparte_numeros(cant_numeros, cant_personas):
    return list(permutations(range(1, cant_numeros+1), cant_personas))
print("Ejercicio 32:")
cant_numeros = 8
cant_personas = 3
print(" Ejercicio 32:")
print(f" Las posibilidades de repartir {cant_numeros} números en {cant_personas} es: ", reparte_numeros(cant_numeros, cant_personas))


#################################################
#        Funciones parciales y Curring          #
#################################################

#
# Ejercicio 33:
# Utilizando la siguiente función:
#  def envolver_texto(prefijo, sufijo, texto):
#      return prefijo + texto + sufijo
#  crear una función, con nombre curried_envolver_texto, que permita currificar la función envolver_texto.
#
def envolver_texto(prefijo, sufijo, texto):
    return prefijo + texto + sufijo

def curried_envolver_texto(prefijo):
    def con_sufijo(sufijo):
        def con_texto(texto):
            return prefijo + texto + sufijo
        return con_texto
    return con_sufijo

envolver_con_barras = curried_envolver_texto("[")("]")
resultado = envolver_con_barras("Hola")
print(" Ejercicio 33:")
print("Resultado de currificar la función dada: " + resultado)  # Salida: [Hola]

#
# Ejercicio 34:
# Crear una serie de funciones currificadas que permitan aplicar varias operaciones a un string, como convertir a mayúsculas, reemplazar palabras, y agregar prefijos o sufijos, cada una en una función que tome un solo argumento.

def agregar_prefijo(prefijo):
    def con_sufijo(sufijo):
        def transformar(texto):
            return prefijo + texto + sufijo
        return transformar
    return con_sufijo

def convertir_mayusculas():
    def transformar(texto):
        return texto.upper()
    return transformar

def reemplazar(palabra_vieja):
    def con_nueva(nueva_palabra):
        def transformar(texto):
            return texto.replace(palabra_vieja, nueva_palabra)
        return transformar
    return con_nueva

# Crear una función que agregue prefijo y sufijo
prefijo_sufijo = agregar_prefijo(">>> ")  # Solo prefijo
sufijo = prefijo_sufijo(" <<<")  # Sufijo añadido

# Convertir a mayúsculas
mayusculas = convertir_mayusculas()

# Reemplazar palabra
reemplazar_hola = reemplazar("Hola")("¡Hola!")

# Procesar todo paso a paso
texto = "Hola amigo"
texto_mayusculas = mayusculas(texto)
texto_reemplazado = reemplazar_hola(texto)
texto_con_prefijo_sufijo = sufijo(texto)

print(" Ejercicio 34:")
print("Funciones currificadas aplicadas a un texto:")
print(texto)
print(texto_upper)                # 'HOLA AMIGO'
print(texto_reemplazado)           # '¡Hola! amigo'
print(texto_con_prefijo_sufijo)    # '>>> Hola amigo <<<'
