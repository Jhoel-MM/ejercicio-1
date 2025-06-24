agenda = {}

def agregar_contacto(nombre, telefonos, email="", direccion=""):
    agenda[nombre] = {
        "telefonos": telefonos,
        "email": email,
        "direccion": direccion
    }
    print(f"Contacto '{nombre}' agregado.")

def buscar_por_nombre(nombre):
    resultado = {}
    for nombre_contacto, datos in agenda.items():
        if nombre.lower() in nombre_contacto.lower():
            resultado[nombre_contacto] = datos
    return resultado

def editar_contacto(nombre, campo, nuevo_valor):
    if nombre in agenda:
        if campo == "telefonos":
            agenda[nombre][campo] = nuevo_valor  # nuevo_valor es lista aquí
        else:
            agenda[nombre][campo] = nuevo_valor
        print(f"Contacto '{nombre}' modificado.")
    else:
        print(f"No se encontró el contacto '{nombre}'.")

def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto '{nombre}' eliminado.")
    else:
        print(f"No se encontró el contacto '{nombre}'.")

def mostrar_contactos():
    if not agenda:
        print("Agenda vacía.")
        return
    for nombre, datos in agenda.items():
        print(f"\nNombre: {nombre}")
        print(f" Teléfonos: {', '.join(datos['telefonos'])}")
        print(f" Email: {datos['email']}")
        print(f" Dirección: {datos['direccion']}")
        print("-------------------")

# Menú interactivo
while True:
    print("\n=== GESTOR DE CONTACTOS ===")
    print("1. Agregar contacto")
    print("2. Buscar contacto por nombre")
    print("3. Editar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar todos los contactos")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    if opcion == '1':
        nombre = input("Nombre del contacto: ")
        telefonos = input("Teléfonos (separados por coma): ").split(",")
        telefonos = [tel.strip() for tel in telefonos]  # limpiar espacios
        email = input("Email (opcional): ")
        direccion = input("Dirección (opcional): ")
        agregar_contacto(nombre, telefonos, email, direccion)

    elif opcion == '2':
        nombre = input("Nombre para buscar: ")
        resultados = buscar_por_nombre(nombre)
        if resultados:
            for nom, datos in resultados.items():
                print(f"\nNombre: {nom}")
                print(f" Teléfonos: {', '.join(datos['telefonos'])}")
                print(f" Email: {datos['email']}")
                print(f" Dirección: {datos['direccion']}")
                print("-------------------")
        else:
            print("No se encontraron contactos con ese nombre.")

    elif opcion == '3':
        nombre = input("Nombre del contacto a editar: ")
        if nombre in agenda:
            print("Campos que puedes editar: telefonos, email, direccion")
            campo = input("Campo a editar: ").lower()
            if campo == "telefonos":
                nuevos_telefonos = input("Nuevo listado de teléfonos (separados por coma): ").split(",")
                nuevos_telefonos = [tel.strip() for tel in nuevos_telefonos]
                editar_contacto(nombre, campo, nuevos_telefonos)
            elif campo in ["email", "direccion"]:
                nuevo_valor = input(f"Nuevo valor para {campo}: ")
                editar_contacto(nombre, campo, nuevo_valor)
            else:
                print("Campo inválido.")
        else:
            print(f"No se encontró el contacto '{nombre}'.")

    elif opcion == '4':
        nombre = input("Nombre del contacto a eliminar: ")
        eliminar_contacto(nombre)

    elif opcion == '5':
        mostrar_contactos()

    elif opcion == '0':
        print("¡Hasta luego!")
        print("Jhoel Ivan Macias Mamani")
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.")
        
