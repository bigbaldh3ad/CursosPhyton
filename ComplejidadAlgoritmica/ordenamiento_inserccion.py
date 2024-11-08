import random

def ordenamiento_por_insercion(lista):
    # Recorre la lista comenzando desde el segundo elemento (índice 1)
    for indice in range(1, len(lista)):
        # Guarda el valor del elemento actual y su posición
        valor_actual = lista[indice]
        posicion_actual = indice

        # Mientras no estemos al principio de la lista y el valor del elemento en la posición anterior sea mayor que el valor actual
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            # Desplaza el elemento hacia la derecha
            lista[posicion_actual] = lista[posicion_actual - 1]
            # Mueve la posición hacia la izquierda
            posicion_actual -= 1

        # Inserta el valor actual en su posición correcta
        lista[posicion_actual] = valor_actual
    
    # Devuelve la lista ordenada
    return lista

if __name__ == '__main__':
    # Solicitar al usuario el tamaño de la lista
    tamano_de_lista = int(input('¿De qué tamaño será la lista? '))

    # Generar una lista de números aleatorios entre 0 y 100 con el tamaño especificado por el usuario
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print('Lista original:', lista)

    # Ordenar la lista utilizando el algoritmo de ordenamiento por inserción
    lista_ordenada = ordenamiento_por_insercion(lista)
    print('Lista ordenada:', lista_ordenada)

