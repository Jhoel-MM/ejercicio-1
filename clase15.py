# --------------------------------------
# ✅ Ejercicio 1: Crear y escribir diario
# --------------------------------------

from datetime import datetime  # Para agregar fecha y hora

# Paso 1: Definimos el nombre del archivo
nombre_archivo = "mi_diario.txt"

# Paso 2: Creamos el archivo desde cero (modo 'w') y escribimos líneas predefinidas
with open(nombre_archivo, "w") as diario_file:
    diario_file.write("Querido diario,\n")
    diario_file.write("Hoy aprendí sobre archivos en Python.\n")
    diario_file.write("El modo 'w' borra todo antes de escribir. ¡Qué miedo!\n")
    diario_file.write("¡Pero también es muy útil para comenzar desde cero!\n")

# Confirmamos al usuario
print("✅ Diario creado y primeras entradas guardadas.")

# --------------------------------------
# ✅ Ejercicio 2: Leer el diario (modo A y B)
# --------------------------------------

# Opción A: Leer todo el contenido de una sola vez
print("\n--- Contenido completo del diario (modo A - read()) ---")
try:
    with open(nombre_archivo, "r") as diario_file:
        contenido = diario_file.read()
    print(contenido)
except FileNotFoundError:
    print(f"❌ Error: El archivo '{nombre_archivo}' no existe.")

# Opción B: Leer el archivo línea por línea (más controlado)
print("\n--- Contenido del diario (modo B - línea por línea) ---")
try:
    with open(nombre_archivo, "r") as diario_file:
        for linea in diario_file:
            print(linea.strip())  # .strip() elimina los saltos de línea '\n'
except FileNotFoundError:
    print(f"❌ Error: El archivo '{nombre_archivo}' no existe.")

# --------------------------------------
# ✅ Ejercicio 3: Añadir entrada desde input()
# --------------------------------------

# Aquí el usuario puede ingresar su propia entrada personalizada
print("\n📝 Vamos a añadir una nueva entrada a tu diario.")
print("Escribe tu entrada (usa varias líneas si quieres). Escribe una línea vacía para terminar.")

# Usamos una lista para recoger múltiples líneas del usuario
lineas_usuario = []
while True:
    linea = input()
    if linea == "":
        break  # Al ingresar una línea vacía, se termina la entrada
    lineas_usuario.append(linea)

# Obtenemos la fecha y hora actual
fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Añadimos las nuevas líneas al diario, en modo 'a' para no borrar lo anterior
print("\n✍️ Añadiendo tu entrada al diario...")
with open(nombre_archivo, "a") as diario_file:
    diario_file.write(f"\n--- Nueva entrada personalizada ({fecha_actual}) ---\n")
    for linea in lineas_usuario:
        diario_file.write(linea + "\n")

print("✅ ¡Tu entrada fue añadida con éxito!")

# --------------------------------------
# ✅ Verificación final: Leer todo el contenido actualizado
# --------------------------------------

print("\n📖 Verificando el contenido final del diario (modo B)...")
try:
    with open(nombre_archivo, "r") as diario_file:
        for linea in diario_file:
            print(linea.strip())
except FileNotFoundError:
    print(f"❌ Error: El archivo '{nombre_archivo}' no existe.")
