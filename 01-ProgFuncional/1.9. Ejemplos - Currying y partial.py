##################################################################################
#                           Currying y partial                                  #
##################################################################################


#La currificación transforma una función en una secuencia de funciones, cada una con un solo argumento, mientras que la aplicación parcial simplemente "congela" algunos argumentos de una función, creando una nueva función con menos argumentos

#
# Ejemplo 1:
# Currying - Permite crear funciones especializadas a partir de funciones más generales.
#

# Currificación (implementación manual, no la típica en Python)
def suma_curry(x):
    def suma_y(y):
        return x + y
    return suma_y

f = suma_curry(3)
resultado_curry = f(2) # 5
print(f"Resultado currificacion: {resultado_curry}")

#
# Ejemplo 2:
# Partial - Permite crear funciones especializadas a partir de funciones más generales.
#

from functools import partial

def multiplicar(x, y):
    return x * y

# Crear una función que multiplica por 5 usando aplicación parcial
multiplicar_por_cinco = partial(multiplicar, 5)

# Aplicar la función con un argumento adicional
resultado = multiplicar_por_cinco(10) # 5 * 10 = 50
print(resultado)

# También se puede llamar directamente
resultado = multiplicar(5, 10)
print(resultado)

#
# Ejemplo 3:
# Partial - .
#
suma_parcial = partial(lambda x, y: x + y, 5)
resultado_parcial = suma_parcial(2) # 7


print(f"Resultado aplicacion parcial: {resultado_parcial}")