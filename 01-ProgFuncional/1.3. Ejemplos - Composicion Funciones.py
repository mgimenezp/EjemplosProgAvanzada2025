##################################################################################
#                            Composición de funciones                            #
##################################################################################

#
# Ejemplo 1:
# Función que permite componer 2 funciones que reciben un parámetro de entrada.
#
def sumar1(x): 
    return x + 1
def duplicar(x): 
    return x * 2
def restar5(x):
    return x - 5
def componer(f, g):
 	return lambda x: f(g(x))
print("Ejemplo 1 - Composición de funciones:")
print(" sumar1(duplicar(3)) = ", componer(sumar1, duplicar)(3))
print(" duplicar(restar5(20)) = ", componer(duplicar, restar5)(20))
print(" restar5(duplicar(20)) = ", componer(restar5, duplicar)(20))
