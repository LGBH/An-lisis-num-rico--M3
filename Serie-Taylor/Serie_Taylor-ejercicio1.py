# Aproximaremos la funcion e^x alrededor de x = 0

import math

# Función para calcular la aproximación de e^x usando la serie de Taylor
def exp_aproximacion(x, n):
    """
    Aproxima el valor de e^x utilizando la serie de Taylor hasta el término n.

    Args:
    - x (float): El valor para el cual se desea calcular e^x.
    - n (int): Número de términos en la serie de Taylor.

    Returns:
    - float: Aproximación de e^x.
    """
    aproximacion = 0

    for i in range(n):
        # Término de la serie de Taylor para e^x
        termino = (x ** i) / math.factorial(i)

        # Agregar el término actual a la aproximación
        aproximacion += termino

    return aproximacion

# Valor de x para el cual queremos aproximar e^x
x_valor = 1.0

# Número de términos en la serie de Taylor (puedes ajustar este valor)
num_terminos = 5

# Calcular la aproximación de e^x usando la serie de Taylor
aproximacion_resultado = exp_aproximacion(x_valor, num_terminos)

# Mostrar resultados
print(f"Aproximación de e^{x_valor} con {num_terminos} términos de la serie de Taylor: {aproximacion_resultado}")
print(f"Valor real de e^{x_valor}: {math.exp(x_valor)}")
