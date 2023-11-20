#Consideremos la ecuacion x = e^-x.
#Primero, necesitamos reorganizar la ecuacion en la forma g(x) = x, donde g(x) es una
#es una funcion que tiene un punto fijo en la solucion de la ecuacion original.

#En este caso, elegimos g(x)= e^-x. Entonces, resolver x = e^-x es equivalente a encontrar
#un punto fijo de g(x) = e^-x

import math

# Definimos la función g(x) = e^{-x}
def g(x):
    return math.exp(-x)

# Implementamos el método del punto fijo
def punto_fijo(g, x0, tol, max_iter):
    """
    :param g: Función de iteración g(x)
    :param x0: Aproximación inicial
    :param tol: Tolerancia, criterio de convergencia
    :param max_iter: Número máximo de iteraciones
    :return: Aproximación de la solución
    """
    # Inicializamos la aproximación inicial
    x = x0

    # Iteramos hasta alcanzar la tolerancia o el número máximo de iteraciones
    for i in range(max_iter):
        # Aplicamos la función de iteración
        x = g(x)

        # Verificamos la convergencia
        if abs(x - g(x)) < tol:
            print(f"Convergencia alcanzada en la iteración {i + 1}.")
            return x

    # Si no converge en el número máximo de iteraciones, imprimimos un mensaje
    print("El método del punto fijo no convergió en el número máximo de iteraciones.")
    return None

# Parámetros del método
tolerancia = 1e-6
iteraciones_maximas = 1000
aprox_inicial = 0.5

# Llamamos al método del punto fijo
solucion = punto_fijo(g, aprox_inicial, tolerancia, iteraciones_maximas)

# Imprimimos la solución si se encontró
if solucion is not None:
    print(f"La solución aproximada es x = {solucion}")

