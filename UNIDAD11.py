def buscar_en_matriz(matriz, valor):
    """
    Busca un valor en una matriz bidimensional y devuelve su posición si se encuentra.
    
    :param matriz: La matriz bidimensional (lista de listas).
    :param valor: El valor a buscar.
    :return: Un mensaje indicando si el valor se encontró y su posición.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"El valor {valor} se encontró en la posición ({i}, {j})."
    return f"El valor {valor} no se encontró en la matriz."

# Definir una matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor_a_buscar = 5

# Realizar la búsqueda
resultado = buscar_en_matriz(matriz, valor_a_buscar)

# Mostrar el resultado
print(resultado)