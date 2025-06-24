# 1. Declaramos una matriz que simula un teclado
teclado = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 0, "#"]
]

# 2. Imprimimos la matriz como cuadrícula
print("▶ MATRIZ DEL TECLADO:\n")
for fila in teclado:
    for elemento in fila:
        # Imprime cada elemento con tabulación, sin salto de línea
        print(elemento, end="\t")
    # Al final de cada fila, hacemos un salto de línea
    print()

# 3. Crear una matriz 5x5 de ceros usando bucles anidados
print("\n▶ MATRIZ 5x5 CON CEROS (usando bucles):\n")
matriz_5x5 = []  # Lista vacía para la matriz

for i in range(5):  # Recorremos 5 filas
    fila = []  # Creamos una nueva fila vacía
    for j in range(5):  # Recorremos 5 columnas
        fila.append(0)  # Añadimos un cero a la fila
    matriz_5x5.append(fila)  # Añadimos la fila completa a la matriz

# Imprimimos la matriz como cuadrícula
for fila in matriz_5x5:
    for elemento in fila:
        print(elemento, end="\t")
    print()

# 4. Crear la misma matriz usando comprensión de listas
print("\n▶ MATRIZ 5x5 CON CEROS (usando comprensión de listas):\n")

# Esta línea crea una matriz 5x5 con ceros de forma compacta
matriz_comprension = [[0 for j in range(5)] for i in range(5)]

# Imprimimos la matriz generada
for fila in matriz_comprension:
    for elemento in fila:
        print(elemento, end="\t")
    print()

# 5. Explicación visual para programadores novatos
print("\nEXPLICACIÓN:")
print('''\nmatriz_comprension = [[0 for j in range(5)] for i in range(5)]\n
↳ Parte interna: [0 for j in range(5)] → crea una fila con cinco ceros
↳ Parte externa: for i in range(5) → repite esa fila cinco veces
Resultado: Una matriz de 5x5 completamente llena de ceros.\n''')

print("\nfin del Programa")
print("---Jhoel Ivan Macias Mamani---")