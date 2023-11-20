# Aproximaremos la funcion sin(x) alrededor de x = 0

import math

# Función para calcular la aproximación del seno usando la serie de Taylor
def sin_aproximacion(x, n):
    """
    Aproxima el valor de sen(x) utilizando la serie de Taylor hasta el término n.

    Args:
    - x (float): El valor para el cual se desea calcular el seno.
    - n (int): Número de términos en la serie de Taylor.

    Returns:
    - float: Aproximación del seno de x.
    """
    aproximacion = 0

    for i in range(n):
        # Término de la serie de Taylor para el seno
        termino = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)

        # Agregar el término actual a la aproximación
        aproximacion += termino

    return aproximacion

# Valor de x para el cual queremos aproximar el seno
x_valor = 0.5

# Número de términos en la serie de Taylor (puedes ajustar este valor)
num_terminos = 5

# Calcular la aproximación del seno usando la serie de Taylor
aproximacion_resultado = sin_aproximacion(x_valor, num_terminos)

# Mostrar resultados
print(f"Aproximación de sin({x_valor}) con {num_terminos} términos de la serie de Taylor: {aproximacion_resultado}")
print(f"Valor real de sin({x_valor}): {math.sin(x_valor)}")
