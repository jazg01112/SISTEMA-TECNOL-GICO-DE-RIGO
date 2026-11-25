class Nodo:
    # Cada nodo guarda un producto y sus dos posibles hijos.
    def __init__(self, producto):
        self.producto = producto
        self.izquierdo = None
        self.derecho = None
