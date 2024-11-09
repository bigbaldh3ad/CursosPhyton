class Queue:
    def __init__(self):
        # Inicializa dos stacks: uno para la entrada y otro para la salida
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, data):
        # Añade un elemento al stack de entrada
        self.inbound_stack.append(data)

    def dequeue(self):
        # Si el stack de salida está vacío, mueve todos los elementos del stack de entrada al stack de salida
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        
        # Devuelve el elemento superior del stack de salida
        return self.outbound_stack.pop()

if __name__ == "__main__":
    # Código para probar la clase Queue
    x = Queue()
    x.enqueue(5)
    x.enqueue(6)
    x.enqueue(7)
    
    # Imprime el estado del stack de entrada después de encolar elementos
    print("Inbound stack after enqueues:", x.inbound_stack)
    
    # Desencola un elemento y muestra el estado de los stacks
    x.dequeue()
    print("Inbound stack after one dequeue:", x.inbound_stack)
    print("Outbound stack after one dequeue:", x.outbound_stack)
    
    # Desencola otro elemento y muestra el estado del stack de salida
    x.dequeue()
    print("Outbound stack after second dequeue:", x.outbound_stack)
