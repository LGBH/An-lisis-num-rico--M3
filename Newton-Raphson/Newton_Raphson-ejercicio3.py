#Tenemos la funcion f(x) = x^3 - 5 y queremos encontrar la raíz

# Definir la función que queremos encontrar la raíz
def funcion(x):
    return x**3 - 5

# Definir la derivada de la función (necesaria para el método de Newton-Raphson)
def derivada_funcion(x):
    return 3 * x**2

# Implementar el método de Newton-Raphson
def newton_raphson(x_inicial, tolerancia, iteraciones_max):
    iteracion = 0
    x_actual = x_inicial
    
    # Iterar hasta que se cumpla la tolerancia o se alcance el número máximo de iteraciones
    while abs(funcion(x_actual)) > tolerancia and iteracion < iteraciones_max:
        # Aplicar la fórmula de Newton-Raphson para obtener la siguiente aproximación
        x_actual = x_actual - funcion(x_actual) / derivada_funcion(x_actual)
        iteracion += 1
    
    # Verificar si se encontró una raíz dentro de la tolerancia
    if abs(funcion(x_actual)) <= tolerancia:
        return x_actual, iteracion
    else:
        # Indicar que el método no converge si se alcanza el número máximo de iteraciones
        print("El método no converge después de", iteracion, "iteraciones.")
        return None, iteracion

# Parámetros iniciales
x_inicial = 1.0
tolerancia = 1e-6
iteraciones_max = 1000

# Aplicar el método de Newton-Raphson
raiz, iteraciones = newton_raphson(x_inicial, tolerancia, iteraciones_max)

# Mostrar resultados
if raiz is not None:
    print("La raíz encontrada es:", raiz)
    print("Número de iteraciones:", iteraciones)
