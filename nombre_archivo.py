import json
import os

# Nombre del archivo JSON
nombre_archivo = "mi_diario.json"

# Crear archivo inicial con entradas base (si no existe)
entradas_iniciales = [
    "Querido diario,",
    "Hoy aprendí sobre archivos en Python.",
    "El modo 'w' borra todo antes de escribir. ¡Qué miedo!"
]

# Si el archivo no existe, lo creamos con entradas iniciales
if not os.path.exists(nombre_archivo):
    with open(nombre_archivo, 'w') as f:
        json.dump(entradas_iniciales, f, indent=4, ensure_ascii=False)
    print("✅ Diario creado con entradas iniciales.")
else:
    print("📘 Diario ya existente encontrado.")

# Leer y mostrar contenido actual
print("\n--- Contenido actual del diario ---")
try:
    with open(nombre_archivo, 'r') as f:
        entradas = json.load(f)
        for entrada in entradas:
            print(f"- {entrada}")
except (FileNotFoundError, json.JSONDecodeError):
    print("❌ No se pudo leer el archivo.")

# Permitir añadir nuevas entradas
print("\n✍️ Escribe tus entradas. Escribe 'SALIR' para finalizar.\n")

while True:
    nueva_entrada = input()
    if nueva_entrada.strip().upper() == "SALIR":
        break

    entradas.append(nueva_entrada)

# Guardar todo nuevamente en el archivo JSON
with open(nombre_archivo, 'w') as f:
    json.dump(entradas, f, indent=4, ensure_ascii=False)

# Mostrar contenido actualizado
print("\n--- Contenido final del diario ---")
for entrada in entradas:
    print(f"- {entrada}")

