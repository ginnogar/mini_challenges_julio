'''2. Ordenamiento simple: Escribe una función que ordene una lista de 5 enteros utilizando cualquier método 
de ordenamiento que prefieras (por ejemplo, burbuja, inserción, selección).'''

def ordenar_burbuja(numeros_a_ordenar):
    n = len(numeros_a_ordenar)
    for i in range(n-1): # Recorre la lista n-1 veces
        for j in range(n-1-i): # Compara elementos adyacentes
            if numeros_a_ordenar[j] > numeros_a_ordenar[j+1]: # Si el elemento actual es mayor que el siguiente
                # Intercambia los elementos
                numeros_a_ordenar[j], numeros_a_ordenar[j+1] = numeros_a_ordenar[j+1], numeros_a_ordenar[j]

# Lista de enteros desordenada
lista = [4, 1, 3, 2, 5]

# Ordenar la lista usando la función
ordenar_burbuja(lista)

# Imprimir la lista ordenada
print(lista)  # Salida esperada: [1, 2, 3, 4, 5]
