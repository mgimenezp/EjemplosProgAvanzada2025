##################################################################################
#               Expresiones lambda y funciones de primera clase                  #
##################################################################################

#
# Ejemplo 1:
# Expresión lambda que duplica un número pasado por parámetro.
#
duplica = lambda x: x * 2
print("Ejemplo 1:")
print(" ", duplica(10))

#
# Ejemplo 2:
# Función que recibe por parámetro otra función y un número y retorna el valor de aplicar 
#  la función al número pasados por parámetros.
#
def transformar(funcion, num):
    return funcion(num)
print("Ejemplo 2:")
print(" ", transformar(duplica, 20))

#
# Ejemplo 3:
# Función que recibe un código y devuelve una función. 
# Por ejemplo: podríamos hacer una función que reciba el signo de un operador númerico y 
#  devuelva la función que realiza la operación. 
#
def dame_operacion(operacion):
    if operacion == '+':
        return lambda x, y: x + y
    elif operacion == '-':
        return lambda x, y: x - y
    elif operacion == '*':
        return lambda x, y: x * y
    elif operacion == '/':
        def divide(x, y):
            return x / y
        return divide       #lambda x, y: x / y
    else:
        return None
print("Ejemplo 3:")
func = dame_operacion('+')
print(" 10 + 6 =", func(10, 6))
func = dame_operacion('/')
print(" 100 / 4 =", func(100, 4))
