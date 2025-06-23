import random

FILAS = 4
COLUMNAS = 4
CANTIDAD_BARCOS = 3

def crear_tablero():
    return [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

# Mostrar tablero 
def mostrar_tablero(tablero, ocultar_barcos=False):
    print("  " + " ".join(str(i + 1) for i in range(COLUMNAS)))
    for i, fila in enumerate(tablero):
        letra = chr(ord('A') + i)
        fila_mostrar = []
        for celda in fila:
            if ocultar_barcos and celda == 1:
                fila_mostrar.append("0")
            elif celda == 0:
                fila_mostrar.append("0")
            elif celda == 1:
                fila_mostrar.append("1")
            elif celda == 2:
                fila_mostrar.append("X")
            elif celda == 3:
                fila_mostrar.append("*")
        print(letra + " " + " ".join(fila_mostrar))

# Convertir coordenada tipo A3 a índices
def coord_a_indices(coord):
    fila = ord(coord[0].upper()) - ord('A')
    columna = int(coord[1:]) - 1
    return fila, columna

# Colocar barcos aleatoriamente
def colocar_barcos(tablero, cantidad):
    colocados = 0
    while colocados < cantidad:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = 1
            colocados += 1

# Disparo con puntuación
def disparar(tablero_objetivo, tablero_disparos, coord, jugador):
    fila, columna = coord_a_indices(coord)
    if tablero_objetivo[fila][columna] == 1:
        tablero_objetivo[fila][columna] = 2
        tablero_disparos[fila][columna] = 2
        print("¡Tocado!")
        return 1
    elif tablero_objetivo[fila][columna] in [0, 3]:
        tablero_objetivo[fila][columna] = 3
        tablero_disparos[fila][columna] = 3
        print("Agua...")
        return 0
    else:
        print("Ya disparaste allí.")
        return 0

# Verificar si quedan barcos
def quedan_barcos(tablero):
    for fila in tablero:
        if 1 in fila:
            return True
    return False

# Juego principal
def juego():
    print("=== Batalla Naval 4x4 ===")
    tablero_jugador = crear_tablero()
    tablero_cpu = crear_tablero()
    tablero_disparos_jugador = crear_tablero()
    tablero_disparos_cpu = crear_tablero()

    colocar_barcos(tablero_jugador, CANTIDAD_BARCOS)
    colocar_barcos(tablero_cpu, CANTIDAD_BARCOS)

    puntuacion_jugador = 0
    puntuacion_cpu = 0
    turno = 1

    while quedan_barcos(tablero_jugador) and quedan_barcos(tablero_cpu):
        print(f"\n--- Turno {turno} ---")
        print("Tu tablero:")
        mostrar_tablero(tablero_jugador)
        print("Tus disparos:")
        mostrar_tablero(tablero_disparos_jugador)

        print(f"Puntuación - Jugador: {puntuacion_jugador} | CPU: {puntuacion_cpu}")

        # Turno del jugador
        while True:
            coord = input("Dispara (ej. A2): ").upper()
            try:
                fila, columna = coord_a_indices(coord)
                if 0 <= fila < FILAS and 0 <= columna < COLUMNAS:
                    break
                else:
                    print("Coordenada fuera de rango.")
            except:
                print("Formato inválido. Usa formato como A1, B3...")

        puntuacion_jugador += disparar(tablero_cpu, tablero_disparos_jugador, coord, "Jugador")

        # Turno del CPU
        while True:
            fila_cpu = random.randint(0, FILAS - 1)
            col_cpu = random.randint(0, COLUMNAS - 1)
            if tablero_jugador[fila_cpu][col_cpu] in [0, 1]:
                break
        coord_cpu = f"{chr(ord('A') + fila_cpu)}{col_cpu + 1}"
        print(f"-- CPU dispara a {coord_cpu}")
        puntuacion_cpu += disparar(tablero_jugador, tablero_disparos_cpu, coord_cpu, "CPU")

        turno += 1

    print("\n=== Fin del juego ===")
    print(f"Puntuación final - Jugador: {puntuacion_jugador} | CPU: {puntuacion_cpu}")
    if puntuacion_jugador > puntuacion_cpu:
        print("¡Ganaste la batalla!")
    else:
        print("La CPU gana.") 

# Ejecutar juego
juego()
