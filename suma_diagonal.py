# Definimos la función que suma los elementos de la diagonal principal de una matriz cuadrada
def sumar_diagonal_principal(matriz):
    """
    Esta función recibe una matriz cuadrada (misma cantidad de filas y columnas)
    y retorna la suma de los elementos en su diagonal principal.

    Ejemplo:
    matriz = [[1, 2],
              [3, 4]]
    diagonal principal: 1 y 4 → suma = 5
    """
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]  # Accede al elemento en la posición (i, i)
    return suma

# Función de prueba para verificar que sumar_diagonal_principal funciona correctamente
def probar_suma_diagonal_principal():
    print("\nProbando sumar_diagonal_principal...")

    # Caso 1: matriz 3x3 con números consecutivos
    m1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
    assert sumar_diagonal_principal(m1) == 15  # 1 + 5 + 9

    # Caso 2: matriz 2x2 con ceros y valores definidos
    m2 = [[10, 0],
          [0, 20]]
    assert sumar_diagonal_principal(m2) == 30  # 10 + 20

    # Caso borde: matriz 1x1
    m3 = [[5]]
    assert sumar_diagonal_principal(m3) == 5  # Solo un elemento en la diagonal

    print("¡Pruebas para sumar_diagonal_principal pasaron!")

# Llamamos a la función para ejecutar las pruebas
probar_suma_diagonal_principal()