# Tenemos la ecuacion x^2 = 2
#Primero, reorganizamos la ecuación en la forma g(x) = x. En este caso, podemos elegir g(x) = 1/2(x+2/x).

# Definimos la función g(x) = 0.5 * (x + 2/x)
def g(x):
    return 0.5 * (x + 2 / x)

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
aprox_inicial = 1.0  # Puedes ajustar la aproximación inicial según sea necesario

# Llamamos al método del punto fijo
solucion = punto_fijo(g, aprox_inicial, tolerancia, iteraciones_maximas)

# Imprimimos la solución si se encontró
if solucion is not None:
    print(f"La solución aproximada es x = {solucion}")

