'''1. Búsqueda en lista ordenada: Implementa una función de búsqueda binaria que determine si un número está en una lista 
ordenada de 10 elementos.'''

def busqueda_binaria(lista, objetivo):
    # Inicializar las variables inicio y fin
    inicio = 0
    fin = len(lista) - 1
    
    # Bucle mientras el inicio sea menor o igual al fin
    while inicio <= fin:
        # Calcular el índice medio
        medio = (inicio + fin) // 2

        # Si el elemento medio es igual al objetivo, devuelve el índice medio
        if lista[medio] == objetivo:
            return medio  
        
        # Si el elemento medio es menor que el objetivo, ajusta el inicio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        
        # Si el elemento medio es mayor que el objetivo, ajusta el fin
        else:
            fin = medio - 1
    
    # Si no se encuentra el objetivo en la lista, devuelve -1
    return -1  

# Lista ordenada de 10 elementos
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Solicitar al usuario que ingrese el número a buscar
numero_a_buscar = int(input("Ingresa el número que deseas buscar en la lista: "))

# Llamar a la función y obtener el resultado
indice = busqueda_binaria(lista_ordenada, numero_a_buscar)

# Mostrar el resultado
if indice != -1:
    print(f"El número {numero_a_buscar} está en el índice {indice}.")
else:
    print(f"El número {numero_a_buscar} no está en la lista.")
