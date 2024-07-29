'''6. Árbol binario de búsqueda (BST): Implementa solo la inserción en un árbol binario de búsqueda para 5 elementos.'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)

# Probar la función de inserción
arbol = BST()
elementos = [7, 3, 10, 1, 5]
for elemento in elementos:
    arbol.insertar(elemento)

def imprimir_en_orden(nodo):
    if nodo is not None:
        imprimir_en_orden(nodo.izquierdo)
        print(nodo.valor, end=' ')
        imprimir_en_orden(nodo.derecho)

imprimir_en_orden(arbol.raiz)  # Salida esperada: 1 3 5 7 10
