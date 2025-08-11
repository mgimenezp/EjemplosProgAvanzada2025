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

# Ejemplo 2: Si no tuvieramos la clausura, no podríamos mantener el estado
def crear_contador_sin_clausura(inicio):
    """Crea un contador sin clausura, lo que no permite mantener el estado."""
    contador = inicio
    def obtener_y_aumentar():
        """Incrementa y devuelve el valor del contador."""
        return contador + 1  # Siempre devuelve el mismo valor
    return obtener_y_aumentar   
