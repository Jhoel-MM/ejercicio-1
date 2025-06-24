# Paso 1: Variables Globales
lista_de_tareas = []
proximo_id_tarea = 1  # Para generar IDs únicos

# Paso 2: Implementar agregar_tarea
def agregar_tarea(descripcion, prioridad="media"):
    global proximo_id_tarea
    nueva_tarea = {
        "id": proximo_id_tarea,
        "descripcion": descripcion,
        "completada": False,
        "prioridad": prioridad
    }
    lista_de_tareas.append(nueva_tarea)
    proximo_id_tarea += 1
    print(f" Tarea '{descripcion}' añadida con éxito.")

# Paso 3: Implementar mostrar_tareas
def mostrar_tareas():
    print("\n--- LISTA DE TAREAS ---")
    if not lista_de_tareas:
        print("¡No hay tareas pendientes! ¡A disfrutar!")
        return

    for tarea in lista_de_tareas:
        estado = "✔" if tarea["completada"] else "✘"
        print(f"{estado} ID: {tarea['id']} | {tarea['descripcion']} (Prioridad: {tarea['prioridad']})")
    print("------------------------")

# Paso 4: Implementar buscar_tarea_por_id
def buscar_tarea_por_id(id_buscado):
    for tarea in lista_de_tareas:
        if tarea["id"] == id_buscado:
            return tarea
    return None

# Paso 5: Marcar tarea como completada
def marcar_tarea_completada(id_tarea):
    tarea = buscar_tarea_por_id(id_tarea)
    if tarea:
        tarea["completada"] = True
        print(f" Tarea '{tarea['descripcion']}' marcada como completada.")
    else:
        print(f" Error: No se encontró la tarea con ID {id_tarea}.")

# Paso 6: Eliminar tarea
def eliminar_tarea(id_tarea):
    tarea = buscar_tarea_por_id(id_tarea)
    if tarea:
        lista_de_tareas.remove(tarea)
        print(f" Tarea '{tarea['descripcion']}' eliminada.")
    else:
        print(f" Error: No se encontró la tarea con ID {id_tarea}.")

# Paso 7: Bucle principal del programa
while True:
    print("\n===== MENÚ TO-DO LIST =====")
    print("1. Agregar nueva tarea")
    print("2. Mostrar todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("0. Salir")
    opcion = input("Elige una opción: ")

    if opcion == '1':
        desc = input("Descripción de la nueva tarea: ")
        prio = input("Prioridad (alta, media, baja): ").lower()
        if prio not in ["alta", "media", "baja"]:
            prio = "media"  # Valor por defecto
        agregar_tarea(desc, prio)
    elif opcion == '2':
        mostrar_tareas()
    elif opcion == '3':
        try:
            id_t = int(input("ID de la tarea a completar: "))
            marcar_tarea_completada(id_t)
        except ValueError:
            print(" Error: Ingresa un número válido.")
    elif opcion == '4':
        try:
            id_t = int(input("ID de la tarea a eliminar: "))
            eliminar_tarea(id_t)
        except ValueError:
            print(" Error: Ingresa un número válido.")
    elif opcion == '0':
        print("¡Hasta pronto!")
        print("-- Jhoel Ivan Macias Mamani --")
        break
    else:
        print(" Opción no válida. Inténtalo de nuevo.")

