# Ejercicio 1: Creando y escribiendo nuestro diario
nombre_archivo = "mi_diario.txt"

with open(nombre_archivo, 'w') as diario_file:
    diario_file.write("Querido diario,\n")
    diario_file.write("Hoy aprendí sobre archivos en Python.\n")
    diario_file.write("El modo 'w' borra todo antes de escribir. ¡Qué miedo!\n")

print("Las entradas iniciales del diario se han guardado.")

# Leer contenido del diario
print("\n--- Contenido del diario ---")
try:
    with open(nombre_archivo, "r") as diario_file:
        for linea in diario_file:
            print(linea.strip())
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe.")

# Añadir entradas del usuario (sin mensajes, sin fecha/hora)
print("\nEscribe tus entradas. Escribe 'SALIR' para finalizar.\n")

while True:
    entrada = input()
    if entrada.strip().upper() == "SALIR":
        break

    with open(nombre_archivo, "a") as diario_file:
        diario_file.write("\n" + entrada + "\n")

# Mostrar contenido final del diario
print("\n--- Contenido final del diario ---")
try:
    with open(nombre_archivo, "r") as diario_file:
        for linea in diario_file:
            print(linea.strip())
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe.")

