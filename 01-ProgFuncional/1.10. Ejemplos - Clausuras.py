##################################################################################
#                           Clausura                                #
##################################################################################

#
# Ejemplo 1:
# Clausura - Contador de enteros
#

def crear_contador(inicio):
  """Crea un contador que recuerda su valor inicial."""
  def obtener_y_aumentar():
    """Incrementa y devuelve el valor del contador."""
    obtener_y_aumentar.contador += 1
    return obtener_y_aumentar.contador
  obtener_y_aumentar.contador = inicio  # Inicializa el contador
  return obtener_y_aumentar

# Crea un contador que empieza en 5
mi_contador = crear_contador(5)

# Llama a la función para obtener y aumentar el contador
print(mi_contador())  # Salida: 6
print(mi_contador())  # Salida: 7