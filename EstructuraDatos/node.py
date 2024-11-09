class Node(object):
    # Representa un nodo enlazado simple.
    def __init__(self, data, next=None):
        # Inicializa el nodo con datos (data) y el enlace al siguiente nodo (next).
        self.data = data
        self.next = next

def run():
    print('**** Forma Manual *****')
    # Crear nodos manualmente y enlazarlos
    nodo3 = Node("C", None)
    nodo2 = Node("B", nodo3)
    nodo1 = Node("A", nodo2)

    # Imprimir los nodos creados manualmente
    print(f'nodo 1: {nodo1}', f'nodo 2: {nodo2}', f'nodo 3: {nodo3}', sep='\n')

    print('**** Forma Iterativa ****')
    head = None
    # Crear nodos iterativamente y enlazarlos
    for count in range(1, 5):
        head = Node(count, head)

    # Imprimir los nodos creados iterativamente
    numero_nodo = 0
    while head != None:
        print(f'nodo {numero_nodo}: {head}', f'; data del nodo {numero_nodo}: {head.data}')
        head = head.next
        numero_nodo = numero_nodo + 1

if __name__ == '__main__':
    run()


    
    
    