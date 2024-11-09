"""
Código utilizado para la clase 'Crear un stack'.
"""

class Node:
    # Representa un nodo en el stack.
    def __init__(self, data=None):
        # Inicializa el nodo con datos (data) y el enlace al siguiente nodo (next).
        self.data = data
        self.next = None

class Stack:
    # Representa un stack (pila) utilizando nodos enlazados.
    def __init__(self):
        # Inicializa el stack con el nodo superior (top) y el tamaño (size).
        self.top = None
        self.size = 0

    def push(self, data):
        # Añade un elemento en la parte superior del stack.
        node = Node(data)

        if self.top:
            # Si el stack no está vacío, enlaza el nuevo nodo al top actual.
            node.next = self.top
            self.top = node
        else:
            # Si el stack está vacío, el nuevo nodo es el top.
            self.top = node

        self.size += 1

    def pop(self):
        # Elimina y devuelve el elemento en la parte superior del stack.
        if self.top:
            # Si el stack no está vacío, guarda los datos del nodo superior.
            data = self.top.data
            self.size -= 1

            if self.top.next:
                # Si hay más nodos en el stack, el top se mueve al siguiente nodo.
                self.top = self.top.next
            else:
                # Si no hay más nodos, el stack queda vacío.
                self.top = None

            return data
        else:
            # Si el stack está vacío, devuelve un mensaje indicando que está vacío.
            return "El stack está vacío"

    def peek(self):
        # Devuelve el elemento en la parte superior del stack sin eliminarlo.
        if self.top:
            return self.top.data
        else:
            return "El stack está vacío"

    def clear(self):
        # Vacía el stack eliminando todos los elementos.
        while self.top:
            self.pop()

if __name__ == "__main__":
    # Código para probar la clase Stack
    pila = Stack()
    pila.push(1)
    pila.push(2)
    pila.push(3)
    print("Elemento en la parte superior después de 3 push:", pila.peek())
    print("Elemento eliminado (pop):", pila.pop())
    print("Elemento en la parte superior después de 1 pop:", pila.peek())
    pila.clear()
    print("Estado del stack después de clear:", pila.peek())
