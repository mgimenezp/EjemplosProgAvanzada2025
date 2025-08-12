##################################################################################
#                                 Decoradores                                    #
##################################################################################

#
# Ejemplo 1:
# Se tiene una función que saluda y se le agrega código que envuelve el mensaje de saludo con un mensaje antes y otro después.
#
def mi_decorador(func):
    def envoltorio():
        print(" Antes de la función")
        func()
        print(" Después de la función")
    return envoltorio
@mi_decorador
def saludar():
    print(" Hola, mundo!")
print("Ejemplo 1:")
saludar()

#
# Ejemplo 2:
# Función que imprime un rango de numeros del 0 hasta el número que se pasa por parámetro.
#
def imprimirNumeros(n):
    print("", end=" ")
    for i in range(n):
        print(i, end=" ")
    print(" ")
print("Ejemplo 2:")
imprimirNumeros(100)

#
# Ejemplo 3: 
# A la función anterior queremos saber cuanto demora al ejecutarse.
#
import time
def imprimirNumeros(n):
    inicio = time.time()
    print("", end=" ")
    for i in range(n):
        print(i, end=" ")
    print(" ")
    final = time.time()
    print(f" Tiempo de ejecución: {final - inicio}")
print("Ejemplo 3:")
imprimirNumeros(100)

# 
# Ejemplo 4: 
# Queremos hacer lo mismo que el ejemplo 3 pero sin modificar la función imprimirNumeros.
# 
import time
def calcularTiempo(funcion):
    def funcionModificada(n):
        inicio = time.time()
        funcion(n)
        final = time.time()
        print(f" Tiempo de ejecución: {final - inicio}")
    return funcionModificada
@calcularTiempo        
def imprimirNumeros(n):
    print("", end=" ")
    for i in range(n):
        print(i, end=" ")
    print(" ")
print("Ejercicio 4:")
imprimirNumeros(100)

# 
# Ejemplo 5: 
# Podriamos tener otras funciones a las que le querermos agregar la información del tiempo de procesamiento.
# 
import time
def calcularTiempo(funcion):
    def funcionModificada(n):
        inicio = time.time()
        funcion(n)
        final = time.time()
        print(f" Tiempo de ejecución: {final - inicio}")
    return funcionModificada
@calcularTiempo        
def imprimirNumeros(n):
    print(" Números = ", end="")
    for i in range(n):
        print(i, end=" ")
    print(" ")
@calcularTiempo
def cuadrado(x):
    val = x * x
    print(" Cuadrado =", val)
    return val

@calcularTiempo
def mitad(x):
    val = x / 2
    print(" Mitad =", val)
    return val
print("Ejercicio 5:")
imprimirNumeros(1000)
cuadrado(40)
mitad(300)

#
# Ejemplo 6:
# total_ordering: Facilita la creación de clases personalizadas que deseen usar operadores de comparación.
#
from functools import total_ordering
@total_ordering
class MiClase:
    def __init__(self, valor):
        self.valor = valor
    def __eq__(self, otro):
        return self.valor == otro.valor
    def __lt__(self, otro):
        return self.valor < otro.valor
objeto1 = MiClase(10)
objeto2 = MiClase(20)
print("Ejercicio 6 - total_ordering:")
print(objeto1 == objeto2)
print(objeto1 < objeto2)
print(objeto1 >= objeto2)

#
# Ejemplo 7:
# lru_cache: Implementa una caché con la estrategia "Least Recently Used".
# Esta caché almacena los resultados de las llamadas a funciones para evitar recálculos costosos, 
#  especialmente útil cuando se trabaja con funciones que reciben argumentos repetidos. 
#
from functools import lru_cache
import time
@lru_cache(maxsize=32)
def expensive_function(arg1, arg2):
    print(" Calculando...")
    time.sleep(1)  # Simula una operación costosa
    return arg1 * arg2
print("Ejercicio 7 - lru_cache:")
# Primera llamada: se calcula el resultado
resultado1 = expensive_function(2, 3)
print(f" Resultado 1: {resultado1}")
# Segunda llamada: se usa el resultado de la caché
resultado2 = expensive_function(2, 3)
print(f" Resultado 2: {resultado2}")
# Tercer llamada: se calcula el resultado de nuevo
resultado4 = expensive_function(5, 2)
print(f" Resultado 3: {resultado4}")

#
# Ejemplo 8: 
# wraps: Se utiliza para preservar los metadatos de una función original cuando se aplica un decorador..
#
from functools import wraps 
def mi_decorador(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f" Llamando a la función {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f" Función {func.__name__} terminada")
        return resultado
    return wrapper
@mi_decorador
def saludar(nombre):
    """Esta función saluda a una persona."""
    print(f" Hola, {nombre}")
print("Ejercicio 8 - wraps:")
print(" __name__ =", saludar.__name__)
print(" __doc__ =", saludar.__doc__)
saludar("Mundo")
