'''3. Recorrido en profundidad (DFS): Implementa un recorrido DFS para un grafo simple con 5 nodos.'''

# Definir el grafo: quí representamos un grafo simple donde cada nodo es una clave en el diccionario y su valor 
# es una lista de nodos adyacentes.
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Función DFS
def dfs(grafo, nodo, visitados): # Función dfs que toma el grafo, el nodo actual y un conjunto de nodos visitados.
    if nodo not in visitados:
        print(nodo)  # Visitar el nodo # Imprimimos el nodo para mostrar que lo hemos visitado.
        visitados.add(nodo) # Agregamos el nodo al conjunto de nodos visitados.
        for vecino in grafo[nodo]: # Recorremos cada vecino del nodo actual.
            dfs(grafo, vecino, visitados)# Llamamos recursivamente a la función dfs para cada vecino no visitado.

# Llamar a la función DFS
visitados = set() # Creamos un conjunto vacío para llevar el seguimiento de los nodos visitados.
dfs(grafo, 'A', visitados) # Llamamos a la función dfs empezando desde el nodo 'A'
