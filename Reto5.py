'''5. Camino más corto: Dado un grafo pequeño con 5 nodos y 6 aristas, escribe una función que encuentre el camino 
más corto entre dos nodos especificados usando cualquier método que prefieras.'''

from collections import deque # Importamos deque de collections para usarlo como una cola eficiente.

# Definir el grafo: Aquí representamos un grafo donde cada nodo es una clave en el diccionario y su valor es una lista 
# de nodos adyacentes.
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Función para encontrar el camino más corto
def bfs_camino_mas_corto(grafo, inicio, objetivo): # Definimos la función que toma el grafo, el nodo de inicio y el nodo objetivo.
    # Inicializamos la cola con una tupla que contiene el nodo de inicio y el camino tomado hasta ahora 
    # (que solo contiene el nodo de inicio).
    cola = deque([(inicio, [inicio])])
    visitados = set()  # Creamos un conjunto vacío para llevar el seguimiento de los nodos visitados.

    while cola: # Mientras la cola no esté vacía:
        nodo, camino = cola.popleft()  # Sacamos el primer nodo y el camino tomado hasta ahora de la cola.
        if nodo == objetivo:  # Si hemos llegado al nodo objetivo
            return camino  # Devolvemos el camino tomado hasta ahora.
        if nodo not in visitados:
            visitados.add(nodo)  # Marcamos el nodo como visitado
            for vecino in grafo[nodo]: # Recorremos cada vecino del nodo actual.
                if vecino not in visitados: 
                    # Añadimos el vecino a la cola con el camino actualizado
                    cola.append((vecino, camino + [vecino]))
    return None  # Si no encontramos un camino, devolvemos None

# Llamar a la función para encontrar el camino más corto
camino = bfs_camino_mas_corto(grafo, 'A', 'F')
print(camino)  # Salida esperada: ['A', 'C', 'F'] o ['A', 'B', 'E', 'F']
