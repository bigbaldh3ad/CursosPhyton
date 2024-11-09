"""
Solucion al reto del profe de una playlist de musicas
"""

import time

class ColaLista:
    def __init__(self):
        # Inicializa una cola basada en listas vacía y su tamaño.
        self.elementos = []
        self.tamaño = 0

    def encolar(self, dato):
        # Añade un elemento al frente de la lista (cola).
        self.elementos.insert(0, dato)
        self.tamaño += 1

    def desencolar(self):
        # Elimina y devuelve el elemento al final de la lista (cola).
        if self.tamaño <= 0:
            return 0
        dato = self.elementos.pop()
        self.tamaño -= 1
        return dato

class ListaReproduccionMusica(ColaLista):
    def __init__(self):
        super().__init__()

    def agregar_canciones(self, cancion: tuple):
        # Añade una canción a la lista de reproducción.
        self.encolar(cancion)

    def reproducir_cancion(self):
        # Reproduce la canción desencolada.
        cancion = self.desencolar()
        if cancion:
            print(f'Reproduciendo: {cancion[0]} por {cancion[1]} min')
            time.sleep(cancion[1])
        else:
            print('No hay más canciones')

    def reproducir_canciones(self):
        # Reproduce todas las canciones en la lista de reproducción.
        while self.elementos:
            self.reproducir_cancion()

    def todas_las_canciones(self):
        # Muestra todas las canciones en la lista de reproducción.
        if self.elementos:
            print('Las canciones en la lista de reproducción son:')
            for i, cancion in enumerate(self.elementos[::-1], start=1):
                print(f'Canción {i}: {cancion[0]}, Duración: {cancion[1]}')
        print(f'Hay {self.tamaño} canciones')
        return self.tamaño

if __name__ == '__main__':
    playlist = ListaReproduccionMusica()

    # Añadir canciones a la lista de reproducción
    playlist.agregar_canciones(("Faded - Alan Walker", 3.32))
    playlist.agregar_canciones(("Alone - Alan Walker", 2.41))
    playlist.agregar_canciones(("Ghost Town - Marmelion", 4.15))
    playlist.agregar_canciones(("Spectre - Alan Walker", 3.50))

    playlist.todas_las_canciones()
    print()

    playlist.reproducir_canciones()
    print()

    playlist.reproducir_cancion()
    playlist.todas_las_canciones()
