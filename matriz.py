def transponer_matriz(matriz):
    if not matriz or not matriz[0]:
        return []
    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    matriz_transpuesta = []
    for j in range(num_columnas):
        nueva_fila = []
        for i in range(num_filas):
            nueva_fila.append(matriz[i][j])
        matriz_transpuesta.append(nueva_fila)
    return matriz_transpuesta

m1 = [[1, 2, 3], [4, 5, 6]]
t1 = transponer_matriz(m1)
assert t1 == [[1, 4], [2, 5], [3, 6]]
print ("Prueba 1 (2x3) pasada")