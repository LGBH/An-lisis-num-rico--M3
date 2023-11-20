#Queremos encontrar la raíz de la función f(x) = x^2 - 4

def funcion(x):
    return x**2 - 4

def derivada_funcion(x):
    return 2 * x

def newton_raphson(x_inicial, tolerancia, iteraciones_max):
    iteracion = 0
    x_actual = x_inicial
    
    while abs(funcion(x_actual)) > tolerancia and iteracion < iteraciones_max:
        x_actual = x_actual - funcion(x_actual) / derivada_funcion(x_actual)
        iteracion += 1
    
    if abs(funcion(x_actual)) <= tolerancia:
        return x_actual, iteracion
    else:
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
