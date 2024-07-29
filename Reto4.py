'''4. Recorrido en amplitud (BFS): Implementa un recorrido BFS para un grafo simple con 5 nodos.'''

from collections import deque # Importamos deque de collections para usarlo como una cola eficiente.

# Definir el grafo: Aquí representamos un grafo simple donde cada nodo es una clave en el diccionario y su valor 
# es una lista de nodos adyacentes.
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Función BFS
def bfs(grafo, inicio): # Definimos la función bfs que toma el grafo y el nodo de inicio.
    visitados = set() # Creamos un conjunto vacío para llevar el seguimiento de los nodos visitados.
    cola = deque([inicio]) # Inicializamos la cola con el nodo de inicio.

    while cola: # Mientras la cola no esté vacía:
        nodo = cola.popleft() # Sacamos el primer nodo de la cola.
        if nodo not in visitados:
            print(nodo) # Imprimimos el nodo para mostrar que lo hemos visitado.
            visitados.add(nodo)  # Agregamos el nodo al conjunto de nodos visitados.
            for vecino in grafo[nodo]: # Recorremos cada vecino del nodo actual.
                if vecino not in visitados: # Si el vecino no ha sido visitado:
                    cola.append(vecino)  # Agregar los vecinos no visitados a la cola

# Llamar a la función BFS
bfs(grafo, 'A')  # Iniciar BFS desde el nodo 'A'
