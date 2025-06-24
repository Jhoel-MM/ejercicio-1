agenda = []
def agregar_contacto():
    nombre = input("Nombre: ")
    telefonos = input("Teléfonos (separados por coma): ").split(",")
    telefonos = [t.strip() for t in telefonos]
    email = input("Email: ")
    direccion = input("Dirección (opcional): ")
    contacto = {
        "nombre": nombre,
        "telefonos": telefonos,
        "email": email,
        "direccion": direccion
    }
    agenda.append(contacto)
    print(f" Contacto '{nombre}' agregado.\n")
def buscar_por_nombre():
    nombre = input("Nombre a buscar: ")
    resultados = [c for c in agenda if c["nombre"].lower() == nombre.lower()]
    if resultados:
        for c in resultados:
            mostrar_un_contacto(c)
    else:
        print(" Contacto no encontrado.\n")
def editar_contacto():
    nombre = input("Nombre del contacto a editar: ")
    for contacto in agenda:
        if contacto["nombre"].lower() == nombre.lower():
            print("Deja vacío cualquier campo que no quieras cambiar.")
            nuevo_nombre = input(f"Nuevo nombre [{contacto['nombre']}]: ") or contacto['nombre']
            nuevos_telefonos = input(f"Nuevos teléfonos (separados por coma) [{', '.join(contacto['telefonos'])}]: ")
            nuevos_telefonos = [t.strip() for t in nuevos_telefonos.split(",")] if nuevos_telefonos else contacto['telefonos']
            nuevo_email = input(f"Nuevo email [{contacto['email']}]: ") or contacto['email']
            nueva_direccion = input(f"Nueva dirección [{contacto['direccion']}]: ") or contacto['direccion']
            contacto.update({
                "nombre": nuevo_nombre,
                "telefonos": nuevos_telefonos,
                "email": nuevo_email,
                "direccion": nueva_direccion
            })
            print(" Contacto actualizado.\n")
            return
    print(" Contacto no encontrado.\n")
def eliminar_contacto():
    nombre = input("Nombre del contacto a eliminar: ")
    global agenda
    original = len(agenda)
    agenda = [c for c in agenda if c["nombre"].lower() != nombre.lower()]
    if len(agenda) < original:
        print(f" Contacto '{nombre}' eliminado.\n")
    else:
        print(" Contacto no encontrado.\n")
def mostrar_contactos():
    if not agenda:
        print("📭 Agenda vacía.\n")
    for c in agenda:
        mostrar_un_contacto(c)
def mostrar_un_contacto(c):
    print(f" {c['nombre']}")
    print(f"   📞 Teléfonos: {', '.join(c['telefonos'])}")
    print(f"   Email: {c['email']}")
    if c['direccion']:
        print(f"   🏠 Dirección: {c['direccion']}")
    print()
def menu():
    while True:
        print(" GESTOR DE CONTACTOS")
        print("1. Agregar contacto")
        print("2. Buscar contacto por nombre")
        print("3. Editar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos los contactos")
        print("6. Salir")
        opcion = input("Elige una opción (1-6): ")
        print()
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_por_nombre()
        elif opcion == "3":
            editar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            mostrar_contactos()
        elif opcion == "6":
            print("Saliendo del gestor. ¡Vuelta pronto!")
            break
        else:
            print("❗ Opción no válida, intenta de nuevo.\n")
# Ejecutar el menú
menu()
print("Realizado por Flavio Rojas.")