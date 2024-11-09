"""
Code used during the class 'Queues basadas en listas'.
"""

class ListQueue:
    def __init__(self):
        # Inicializa una cola basada en listas vacía y su tamaño
        self.items = []
        self.size = 0

    def enqueue(self, data):
        # Añade un elemento al frente de la lista (cola)
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        # Elimina y devuelve el elemento al final de la lista (cola)
        data = self.items.pop()
        self.size -= 1
        return data

    def traverse(self):
        # Recorre e imprime los elementos de la cola
        for item in range(self.size):
            print(self.items[item])

if __name__ == "__main__":
    # Código para probar la clase ListQueue en el shell
    x = ListQueue()
    x.enqueue('eggs')
    x.enqueue('ham')
    x.enqueue('spam')

    # Imprimir los elementos en la cola
    for i in range(x.size):
        print(x.items[i])
