import random

def ordenamiento_por_mezcla(lista):
    # Si la longitud de la lista es mayor que 1, se procede con el ordenamiento
    if len(lista) > 1:
        # Encontrar el punto medio de la lista
        medio = len(lista) // 2
        # Dividir la lista en dos mitades
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)

        # Llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0  # Iterador para la sublista izquierda
        j = 0  # Iterador para la sublista derecha
        # Iterador para la lista principal
        k = 0

        # Recorrer ambas sublistas y combinar en lista
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Verificar si queda algún elemento en la sublista izquierda
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        # Verificar si queda algún elemento en la sublista derecha
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)

    # Devolver la lista ordenada
    return lista

if __name__ == '__main__':
    # Solicitar al usuario el tamaño de la lista
    tamano_de_lista = int(input('¿De qué tamaño será la lista? '))

    # Generar una lista de números aleatorios entre 0 y 100 con el tamaño especificado por el usuario
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print('Lista original:', lista)
    print('-' * 20)

    # Ordenar la lista utilizando el algoritmo de ordenamiento por mezcla
    lista_ordenada = ordenamiento_por_mezcla(lista)
    print('Lista ordenada:', lista_ordenada)
