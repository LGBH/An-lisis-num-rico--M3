# encontrar la raíz de una función utilizando el método de bisección. Supongamos que queremos encontrar la raíz de la función 
# f(x) = x^2 −4 en el intervalo [0, 3].


def funcion(x):
    return x**2 - 4

def biseccion(a, b, tolerancia):
    # Verifica si la función cambia de signo en el intervalo [a, b]
    if funcion(a) * funcion(b) > 0:
        print("La función no cambia de signo en el intervalo dado.")
        return None

    iteracion = 0
    # Aplica el método de bisección hasta que la diferencia entre a y b sea menor que la tolerancia
    while (b - a) / 2 > tolerancia:
        c = (a + b) / 2  # Calcula el punto medio del intervalo [a, b]

        # Verifica si c es una raíz exacta
        if funcion(c) == 0:
            break
        elif funcion(c) * funcion(a) < 0:
            b = c  # Actualiza el extremo superior del intervalo
        else:
            a = c  # Actualiza el extremo inferior del intervalo

        iteracion += 1

    return c, iteracion

# Intervalo inicial [0, 3]
a = 0
b = 3
tolerancia = 0.0001

resultado = biseccion(a, b, tolerancia)

if resultado:
    raiz, iteraciones = resultado
    print(f"La raíz aproximada es: {raiz}")
    print(f"Se realizaron {iteraciones} iteraciones.")
