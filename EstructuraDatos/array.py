class Array(object):
    "Representa un array."

    def __init__(self, capacidad, valor_relleno=None):
        """
        Args:
            capacidad (int): tamaño estático del array.
            valor_relleno (cualquier tipo, opcional): valor en cada posición. Por defecto es None.
        """
        self.elementos = list()
        for i in range(capacidad):
            self.elementos.append(valor_relleno)

    def __len__(self):
        """Devuelve la capacidad del array."""
        return len(self.elementos)

    def __str__(self):
        """Devuelve la representación en cadena del array."""
        return str(self.elementos)

    def __iter__(self):
        """Soporta el recorrido con un bucle for."""
        return iter(self.elementos)

    def __getitem__(self, indice):
        """Operador de subíndice para acceso en el índice."""
        return self.elementos[indice]

    def __setitem__(self, indice, nuevo_elemento):
        """Operador de subíndice para reemplazo en el índice."""
        self.elementos[indice] = nuevo_elemento

if __name__ == "__main__":
    # Crear una instancia de la clase Array con una capacidad de 5 elementos
    mi_array = Array(5, 0)
    print("Array inicial:", mi_array)

    # Asignar valores a cada elemento del array
    for i in range(len(mi_array)):
        mi_array[i] = i + 1
    print("Array después de asignaciones:", mi_array)

    # Acceder a elementos específicos del array
    print("Elemento en el índice 0:", mi_array[0])
    print("Elemento en el índice 2:", mi_array[2])

    # Reemplazar un elemento en el array
    mi_array[2] = 100
    print("Array después del reemplazo:", mi_array)
