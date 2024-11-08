import random

def busqueda_lineal(lista, objetivo):
    # Inicializamos la variable match en False para indicar que aún no hemos encontrado el objetivo.
    match = False

    # Recorremos cada elemento en la lista.
    for elemento in lista:  # Complejidad O(n)
        
        # Si el elemento actual es igual al objetivo, actualizamos match a True y salimos del bucle.
        if elemento == objetivo:
            match = True
            break

    # Devolvemos True si encontramos el objetivo, False en caso contrario.
    return match

if __name__ == '__main__':
    
    # Solicitamos al usuario que ingrese el tamaño de la lista.
    tamano_de_lista = int(input('¿De qué tamaño será la lista? '))
    
    # Solicitamos al usuario que ingrese el número que desea encontrar.
    objetivo = int(input('¿Qué número quieres encontrar? '))

    # Generamos una lista de números aleatorios entre 0 y 100 con el tamaño especificado por el usuario.
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    # Realizamos la búsqueda lineal del número objetivo en la lista.
    encontrado = busqueda_lineal(lista, objetivo)

    # Imprimimos la lista generada.
    print(lista)
    
    # Informamos al usuario si el número objetivo está o no en la lista.
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')
