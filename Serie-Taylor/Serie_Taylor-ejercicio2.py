# Aproximaremos la funcion ln(x+1) alrededor de x = 0

import math

# Función para calcular la aproximación de ln(x+1) usando la serie de Taylor
def ln_aproximacion(x, n):
    """
    Aproxima el valor de ln(x+1) utilizando la serie de Taylor hasta el término n.

    Args:
    - x (float): El valor para el cual se desea calcular ln(x+1).
    - n (int): Número de términos en la serie de Taylor.

    Returns:
    - float: Aproximación de ln(x+1).
    """
    # Verificar si x está dentro del dominio válido para ln(x+1)
    if x < -1:
        raise ValueError("El argumento de ln(x+1) debe ser mayor o igual a -1.")

    # Calcular la aproximación solo si x está en el dominio válido
    aproximacion = 0

    for i in range(1, n + 1):
        # Término de la serie de Taylor para ln(x+1)
        termino = ((-1) ** (i - 1)) * (x ** i) / i

        # Agregar el término actual a la aproximación
        aproximacion += termino

    return aproximacion

# Valor de x para el cual queremos aproximar ln(x+1)
x_valor = 0.5

# Número de términos en la serie de Taylor (puedes ajustar este valor)
num_terminos = 5

# Calcular la aproximación de ln(x+1) usando la serie de Taylor
aproximacion_resultado = ln_aproximacion(x_valor, num_terminos)

# Mostrar resultados
print(f"Aproximación de ln({x_valor}+1) con {num_terminos} términos de la serie de Taylor: {aproximacion_resultado}")
print(f"Valor real de ln({x_valor}+1): {math.log(x_valor + 1)}")



