import random

# Creación de listas con diferentes elementos
[]
["Isabel"]
["Isabel", "Mulan"]
["Isabel", "Mulan", 255]
["Isabel", ["Mulan", 255]]

# Operaciones típicas de estructuras de datos en Python
frutas = []
frutas.append("Kiwi")
frutas.append("Baya")
frutas.append("Melón")
frutas.sort()  # Ordenar la lista
frutas.pop()  # Eliminar el último elemento
frutas.insert(0, "Manzana")  # Insertar en la primera posición
frutas.insert(1, "Fresa")  # Insertar en la segunda posición
frutas.pop(1)  # Eliminar el elemento en la segunda posición
frutas.remove("Manzana")  # Eliminar el elemento "Manzana"
# frutas.remove("Fruta del dragón")  # Esta línea está comentada y no se ejecutará

def suma_piramidal(inferior, superior, margen = 0):
    """Devuelve la suma de los números desde inferior hasta superior,
    y muestra un rastro de los argumentos y valores de retorno
    en cada llamada."""
    espacios = " " * margen
    print(espacios, inferior, superior)  # Imprimir los argumentos

    if inferior > superior:
        print(espacios, 0)  # Imprimir el valor retornado
        return 0
    else:
        resultado = inferior + suma_piramidal(inferior + 1, superior, margen + 4)
        print(espacios, resultado)  # Imprimir el valor retornado
        return resultado

suma_piramidal(1, 4)
