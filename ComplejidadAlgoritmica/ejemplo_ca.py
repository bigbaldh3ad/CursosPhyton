import math
import time

# O(1) - Constante
def constante():
    # Esta función realiza una operación que siempre toma el mismo tiempo, independientemente del tamaño de la entrada.
    print("O(1):", 42)

# O(n) - Lineal
def lineal(n):
    # Esta función realiza una operación que crece linealmente con el tamaño de la entrada.
    print("O(n):", end=" ")
    for i in range(n):
        # Imprime números de 0 a n-1
        print(i, end=" ")
    print()

# O(log n) - Logarítmica
def logaritmica(n):
    # Esta función realiza una operación que crece logarítmicamente con el tamaño de la entrada.
    print("O(log n):", end=" ")
    i = 1
    while i < n:
        # Imprime valores que son potencias de 2 menores que n
        print(i, end=" ")
        i *= 2
    print()

# O(n log n) - Log Lineal
def log_lineal(n):
    # Esta función realiza una operación que crece en proporción a n * log(n).
    print("O(n log n):", end=" ")
    for i in range(n):
        j = 1
        while j < n:
            # Imprime una combinación de i y j
            print(j, end=" ")
            j *= 2
    print()

# O(n^2) - Cuadrática
def cuadratica(n):
    # Esta función realiza una operación que crece cuadráticamente con el tamaño de la entrada.
    print("O(n^2):", end=" ")
    for i in range(n):
        for j in range(n):
            # Imprime el producto de i y j
            print(i * j, end=" ")
    print()

# O(2^n) - Exponencial
def exponencial(n):
    # Esta función realiza una operación que crece exponencialmente con el tamaño de la entrada.
    print("O(2^n):", end=" ")
    def exp_helper(x):
        if x == 0:
            return 1
        # Cada llamada se descompone en dos llamadas adicionales, duplicando el trabajo en cada nivel
        return exp_helper(x - 1) + exp_helper(x - 1)
    
    exp_helper(n)
    print(f"Terminado para n = {n}")

# Función principal para ejecutar todos los ejemplos
def main(n):
    # Medir y ejecutar la función constante
    start = time.time()
    constante()
    end = time.time()
    print(f"Tiempo O(1): {end - start:.6f} segundos\n")

    # Medir y ejecutar la función lineal
    start = time.time()
    lineal(n)
    end = time.time()
    print(f"Tiempo O(n): {end - start:.6f} segundos\n")

    # Medir y ejecutar la función logarítmica
    start = time.time()
    logaritmica(n)
    end = time.time()
    print(f"Tiempo O(log n): {end - start:.6f} segundos\n")

    # Medir y ejecutar la función log lineal
    start = time.time()
    log_lineal(n)
    end = time.time()
    print(f"Tiempo O(n log n): {end - start:.6f} segundos\n")

    # Medir y ejecutar la función cuadrática
    start = time.time()
    cuadratica(n)
    end = time.time()
    print(f"Tiempo O(n^2): {end - start:.6f} segundos\n")

    # Medir y ejecutar la función exponencial
    start = time.time()
    exponencial(n)
    end = time.time()
    print(f"Tiempo O(2^n): {end - start:.6f} segundos\n")

# Ejecuta la función principal con n = 5
main(5)
