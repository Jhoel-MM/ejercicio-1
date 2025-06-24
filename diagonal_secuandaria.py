# Función que suma los elementos de la diagonal secundaria de una matriz cuadrada
def sumar_diagonal_secundaria(matriz):
    """
    Recibe una matriz cuadrada (misma cantidad de filas y columnas)
    y devuelve la suma de los elementos en la diagonal secundaria.
    La diagonal secundaria va desde la esquina superior derecha
    hasta la esquina inferior izquierda.
    """
    n = len(matriz)  # Número de filas (y columnas)
    suma = 0
    for i in range(n):
        suma += matriz[i][n - 1 - i]  # Elemento en la diagonal secundaria
    return suma


# Función de pruebas para validar que sumar_diagonal_secundaria funciona correctamente
def probar_suma_diagonal_secundaria():
    print("\nProbando sumar_diagonal_secundaria...\n")

    # Caso 1: matriz 3x3
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    esperado1 = 15  # 3 + 5 + 7
    resultado1 = sumar_diagonal_secundaria(m1)
    print("Matriz m1:", m1)
    print("Esperado:", esperado1, "| Obtenido:", resultado1)
    print("✅ PASA" if resultado1 == esperado1 else "❌ NO PASA", "\n")

    # Caso 2: matriz 2x2
    m2 = [[10, 1], [2, 20]]
    esperado2 = 3  # 1 + 2
    resultado2 = sumar_diagonal_secundaria(m2)
    print("Matriz m2:", m2)
    print("Esperado:", esperado2, "| Obtenido:", resultado2)
    print("✅ PASA" if resultado2 == esperado2 else "❌ NO PASA", "\n")

    # Caso 3: matriz 1x1
    m3 = [[42]]
    esperado3 = 42
    resultado3 = sumar_diagonal_secundaria(m3)
    print("Matriz m3:", m3)
    print("Esperado:", esperado3, "| Obtenido:", resultado3)
    print("✅ PASA" if resultado3 == esperado3 else "❌ NO PASA", "\n")

    print("✔️ ¡Todas las pruebas finalizadas!")


# Llamamos a la función de prueba
probar_suma_diagonal_secundaria()
