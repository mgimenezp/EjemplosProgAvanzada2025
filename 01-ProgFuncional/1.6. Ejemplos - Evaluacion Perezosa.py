##################################################################################
#                           Evaluación perezosa                                  #
##################################################################################

#
# Ejemplo 1:
# Iterador perezoso que permite generar los números de Fibonacci de forma infinita, utilizando una clase personalizada.
#
from collections.abc import Iterable
class Fibonacci(Iterable):
    def __init__(self):
        self.a, self.b = 0, 1
        self.total = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        self.total += self.a
        return self.a
    def running_sum(self):
        return self.total
print("Ejemplo 1 - Iterador Fibonacci usando clase personalizada:")
fib = Fibonacci()
print(" SumaTotal(0) =", fib.running_sum())
print("", end=" ")
for indice, valor in zip(range(1,11), fib):
    print(f"Fib({indice}) =", valor, end=" ")
print(" ")
print(" SumaTotal(10) =", fib.running_sum())
print(" Fib(10) =", next(fib))

#
# Ejemplo 2:
# Iterador perezoso que permite generar los números de Fibonacci de forma infinita, utilizando función generadora.
#
def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b
print("Ejemplo 2 - Iterador Fibonacci usando función generadora:")
print("", end=" ")
for indice, valor in zip(range(1,11), fibonacci()):
    print(f"Fib({indice}) =", valor, end=" ")
print(" ")

#
# Ejemplo 3:
# Rutina que duplica el valor de una lista si es impar sino deja el mismo valor, usando comprensión de generador.
# Ejemplo mostrado antes.
#
datos = range(1,1000000000)
generador = (d if d % 2 == 0 else d * 2 for d in datos)
print("Ejemplo 3 - Con comprensión de generador:")
print(" ", end="")
for indice, num in zip(range(1,10), generador):
    print(num, end=" ")
print(" ")

#
# Ejemplo 4:
# Rutina que duplica el valor de una lista si es impar sino deja el mismo valor, usando función generadora.
#
def obtener_numero(datos):
    for elem in datos:
        if elem % 2 == 0:
            yield elem
        else:
            yield elem * 2
generador_imp = obtener_numero(datos)
print("Ejemplo 4 - Versión función generadora:")
print(" ", end="")
for indice, num in zip(range(1,10), generador_imp):
    print(num, end=" ")
print(" ")

#
# Ejemplo 5:
# Rutina que duplica el valor de una lista si es impar sino deja el mismo valor, usando iterador por clase personalizada.
#
class Numeros(object):
    def __init__(self, datos):
        self.datos = datos
        self.i = None
    def __iter__(self):
        return self
    def __next__(self):
        if self.i is None:
            self.i = 0
        else:
            self.i += 1
        try:
            if self.datos[self.i] % 2 == 0:
                return self.datos[self.i]
            else:
                return self.datos[self.i] * 2
        except:
            raise StopIteration
generador_clase = Numeros(datos)
print("Ejemplo 5 - Versión de iterador por clase personalizada:")
print(" ", end="")
for indice, num in zip(range(1,10), generador_clase):
    print(num, end=" ")
print(" ")
