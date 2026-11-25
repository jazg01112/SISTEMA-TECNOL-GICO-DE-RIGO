from models.nodo import Nodo

class ArbolBinario:
    # El ID del producto se utiliza como clave para ordenar el árbol.
    def __init__(self):
        self.raiz = None

    def insertar(self, producto):
        nuevo = Nodo(producto)

        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz
        while True:
            if producto[0] < actual.producto[0]:
                if actual.izquierdo is None:
                    actual.izquierdo = nuevo
                    return
                actual = actual.izquierdo
            elif producto[0] > actual.producto[0]:
                if actual.derecho is None:
                    actual.derecho = nuevo
                    return
                actual = actual.derecho
            else:
                raise ValueError("Ya existe un producto con ese ID.")

    def buscar(self, id_producto):
        actual = self.raiz

        while actual is not None:
            if id_producto == actual.producto[0]:
                return actual.producto
            if id_producto < actual.producto[0]:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        return None

    def eliminar(self, id_producto):
        self.raiz = self._eliminar_nodo(self.raiz, id_producto)

    def _eliminar_nodo(self, nodo, id_producto):
        if nodo is None:
            return None

        if id_producto < nodo.producto[0]:
            nodo.izquierdo = self._eliminar_nodo(nodo.izquierdo, id_producto)
        elif id_producto > nodo.producto[0]:
            nodo.derecho = self._eliminar_nodo(nodo.derecho, id_producto)
        else:
            # Caso 1: el nodo no tiene hijo izquierdo.
            if nodo.izquierdo is None:
                return nodo.derecho

            # Caso 2: el nodo no tiene hijo derecho.
            if nodo.derecho is None:
                return nodo.izquierdo

            # Caso 3: tiene dos hijos. Se busca el menor del subárbol derecho.
            sucesor = self._menor(nodo.derecho)
            nodo.producto = sucesor.producto
            nodo.derecho = self._eliminar_nodo(
                nodo.derecho, sucesor.producto[0]
            )

        return nodo

    def _menor(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

    def recorrido_inorden(self):
        productos = []
        self._inorden(self.raiz, productos)
        return productos

    def _inorden(self, nodo, productos):
        if nodo is not None:
            self._inorden(nodo.izquierdo, productos)
            productos.append(nodo.producto)
            self._inorden(nodo.derecho, productos)
