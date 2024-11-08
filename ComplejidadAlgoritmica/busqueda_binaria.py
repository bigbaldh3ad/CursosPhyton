import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    # Imprime el rango actual en el que se está buscando el objetivo.
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    
    # Si el índice de comienzo es mayor que el índice de final, significa que no se encontró el objetivo.
    if comienzo > final:
        return False

    # Calcula el índice medio del rango actual.
    medio = (comienzo + final) // 2

    # Si el elemento en el índice medio es igual al objetivo, se encontró el objetivo.
    if lista[medio] == objetivo:
        return True
    
    # Si el elemento en el índice medio es menor que el objetivo, busca en la mitad derecha.
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    
    # Si el elemento en el índice medio es mayor que el objetivo, busca en la mitad izquierda.
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

if __name__ == '__main__':
    # Solicitamos al usuario que ingrese el tamaño de la lista.
    tamano_de_lista = int(input('¿De qué tamaño es la lista? '))
    
    # Solicitamos al usuario que ingrese el número que desea encontrar.
    objetivo = int(input('¿Qué número quieres encontrar? '))

    # Generamos una lista de números aleatorios entre 0 y 100 con el tamaño especificado por el usuario y la ordenamos.
    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    # Realizamos la búsqueda binaria del número objetivo en la lista.
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    # Imprimimos la lista generada.
    print(lista)
    # Informamos al usuario si el número objetivo está o no en la lista.
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')
