import random

def ordenamiento_de_burbuja(lista):
    # Obtener el tamaño de la lista
    n = len(lista)

    # Bucle externo: recorre toda la lista
    for i in range(n):
        # Bucle interno: recorre la lista desde el principio hasta el n-i-1
        for j in range(0, n - i - 1):  # O(n) * O(n) = O(n * n) = O(n**2)
            # Si el elemento actual es mayor que el siguiente, intercambiamos los elementos
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Intercambio de elementos

    # Devolver la lista ordenada
    return lista

if __name__ == '__main__':
    # Solicitar al usuario el tamaño de la lista
    tamano_de_lista = int(input('¿De qué tamaño será la lista? '))

    # Generar una lista de números aleatorios entre 0 y 100 con el tamaño especificado por el usuario
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print('Lista original:', lista)

    # Ordenar la lista utilizando el algoritmo de ordenamiento de burbuja
    lista_ordenada = ordenamiento_de_burbuja(lista)
    print('Lista ordenada:', lista_ordenada)
