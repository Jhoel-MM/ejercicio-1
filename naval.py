import random
import json

TAM, NUM_BARCOS, INTENTOS = 5, 3, 10
LETRAS = ['A', 'B', 'C', 'D', 'E']

# Función para crear un tablero vacío
def crear_tablero(): return [['~']*TAM for _ in range(TAM)]

# Función para mostrar el tablero
def mostrar(tablero):
    print("   " + " ".join(str(i+1) for i in range(TAM)))
    for i, fila in enumerate(tablero):
        print(f"{LETRAS[i]}  " + " ".join(fila))

# Función para colocar los barcos en el tablero
def colocar_barcos(tablero):
    for _ in range(NUM_BARCOS):
        while True:
            f, c = random.randint(0, TAM-1), random.randint(0, TAM-1)
            if tablero[f][c] != 'B':
                tablero[f][c] = 'B'
                break

# Función para pedir la coordenada al jugador
def pedir_coord(nombre):
    while True:
        coord = input(f"{nombre}, coordenada (A1-E5): ").upper()
        if len(coord) >= 2 and coord[0] in LETRAS and coord[1:].isdigit():
            f, c = LETRAS.index(coord[0]), int(coord[1:]) - 1
            if 0 <= c < TAM: return f, c
        print("❌ Coordenada inválida.")

# Función para realizar un disparo
def disparo(nombre, visible, oculto):
    mostrar(visible)
    f, c = pedir_coord(nombre)
    if visible[f][c] != '~':
        print("⚠️ Ya elegiste eso.")
        return 0
    if oculto[f][c] == 'B':
        print("🔥 ¡Tocado!")
        visible[f][c] = 'X'
        return 1
    else:
        print("🌊 Agua.")
        visible[f][c] = 'O'
        return 0

# Función para revelar los barcos en el tablero
def revelar(visible, oculto):
    for i in range(TAM):
        for j in range(TAM):
            if oculto[i][j] == 'B' and visible[i][j] == '~':
                visible[i][j] = '🚢'

# Función para guardar puntajes en un archivo JSON
def guardar_puntajes(nombres, puntajes):
    try:
        # Intentar cargar el archivo JSON si existe
        with open('puntajes.json', 'r') as f:
            datos = json.load(f)
    except FileNotFoundError:
        datos = {}

    # Guardar el puntaje actual
    datos[nombres[0]] = puntajes[0]
    datos[nombres[1]] = puntajes[1]

    # Escribir de nuevo en el archivo JSON
    with open('puntajes.json', 'w') as f:
        json.dump(datos, f, indent=4)

# Función principal para jugar
def jugar():
    print("1. Contra bot\n2. 2 jugadores")
    modo = input("Elige modo: ")

    if modo == '2':
        n1, n2 = input("Jugador 1: "), input("Jugador 2: ")
        vis = [crear_tablero(), crear_tablero()]
        occ = [crear_tablero(), crear_tablero()]
        colocar_barcos(occ[0]); colocar_barcos(occ[1])
        pts = [0, 0]; turno = 0

        for _ in range(INTENTOS):
            print(f"\n🎯 Turno de {n1 if turno==0 else n2}")
            pts[turno] += disparo([n1, n2][turno], vis[turno], occ[1-turno])
            if pts[turno] == NUM_BARCOS: break
            turno = 1 - turno

        print(f"\n🟢 {n1}: {pts[0]} | 🟣 {n2}: {pts[1]}")
        if pts[0] > pts[1]: print(f"🏆 ¡Gana {n1}!")
        elif pts[1] > pts[0]: print(f"🏆 ¡Gana {n2}!")
        else: print("🤝 ¡Empate!")
        for i in range(2):
            print(f"\nBarcos de {[n2, n1][i]}:")
            revelar(vis[i], occ[1-i])
            mostrar(vis[i])

        # Guardar los puntajes
        guardar_puntajes([n1, n2], pts)

    else:
        nombre = input("Tu nombre: ")
        vis, occ = crear_tablero(), crear_tablero()
        colocar_barcos(occ)
        aciertos = 0

        for _ in range(INTENTOS):
            aciertos += disparo(nombre, vis, occ)
            if aciertos == NUM_BARCOS: break

        if aciertos == NUM_BARCOS:
            print("🎉 ¡Hundiste todos los barcos!")
        else:
            print("💥 Sin intentos. Perdiste.")
        print("\n🔍 Posiciones reales:")
        revelar(vis, occ)
        mostrar(vis)

        # Guardar el puntaje
        guardar_puntajes([nombre], [aciertos])

if __name__ == "__main__":
    jugar()