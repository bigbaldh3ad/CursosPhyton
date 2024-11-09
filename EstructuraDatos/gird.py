class Array(object):
    # Representa un array unidimensional.

    def __init__(self, capacidad, valor_relleno=None):
        # Inicializa el array con una capacidad fija y un valor de relleno opcional.
        # Args:
        #     capacidad (int): tamaño estático del array.
        #     valor_relleno (cualquier tipo, opcional): valor en cada posición. Por defecto es None.
        self.elementos = [valor_relleno] * capacidad

    def __len__(self):
        # Devuelve la capacidad del array.
        return len(self.elementos)

    def __str__(self):
        # Devuelve la representación en cadena del array.
        return str(self.elementos)

    def __iter__(self):
        # Soporta el recorrido con un bucle for.
        return iter(self.elementos)

    def __getitem__(self, indice):
        # Operador de subíndice para acceso en el índice.
        return self.elementos[indice]

    def __setitem__(self, indice, nuevo_elemento):
        # Operador de subíndice para reemplazo en el índice.
        self.elementos[indice] = nuevo_elemento

class Grid(object):
    # Representa un array bidimensional.
    
    def __init__(self, filas, columnas, valor_relleno=None):
        # Inicializa la rejilla con un número fijo de filas y columnas, y un valor de relleno opcional.
        self.data = Array(filas)
        for fila in range(filas):
            self.data[fila] = Array(columnas, valor_relleno)

    def get_height(self):
        # Devuelve el número de filas.
        return len(self.data)

    def get_width(self):
        # Devuelve el número de columnas.
        return len(self.data[0])

    def __getitem__(self, indice):
        # Soporta el acceso bidimensional con [fila][columna].
        return self.data[indice]

    def __str__(self):
        # Devuelve una representación en cadena de la rejilla.
        resultado = ""
        for fila in range(self.get_height()):
            for col in range(self.get_width()):
                resultado += str(self.data[fila][col]) + " "
            resultado += "\n"
        return str(resultado)

if __name__ == "__main__":
    # Código para probar la clase Grid
    matriz = Grid(3, 3)
    print("Matriz inicial:")
    print(matriz)
    
    for fila in range(matriz.get_height()):
        for columna in range(matriz.get_width()):
            matriz[fila][columna] = fila * columna
    
    print("Matriz después de asignaciones:")
    print(matriz)
    print("Altura de la matriz:", matriz.get_height())
    print("Ancho de la matriz:", matriz.get_width())
    print("Elemento en [1][2]:", matriz[1][2])
    
    matriz[1][2] = 100
    print("Elemento en [1][2] después del reemplazo:", matriz[1][2])
    print("Matriz final:")
    print(matriz)
