# 1. Crea una lista vacía llamada inventario.
inventario = []

# 2. Crea al menos tres diccionarios diferentes, cada uno representando un producto.
producto1 = {
    "nombre": "Chocolate para Taza 'El Ceibo'",
    "precio": 25.50,
    "stock": 50,
    "descripcion": "Delicioso chocolate boliviano para preparar tu taza."
}

producto2 = {
    "nombre": "Café de los Yungas",
    "precio": 40.00,
    "stock": 100,
    "descripcion": "Café orgánico de alta calidad de los Yungas de Bolivia."
}

producto3 = {
    "nombre": "Quinua Real en Grano",
    "precio": 30.75,
    "stock": 80,
    "descripcion": "Quinua real boliviana, ideal para una alimentación saludable."
}

# 3. Añade cada uno de esos diccionarios a la lista inventario usando el método .append().
inventario.append(producto1)
inventario.append(producto2)
inventario.append(producto3)

# 4. Imprime la cantidad de tipos de producto en el inventario (la longitud de la lista).
print(f"Cantidad de tipos de producto en el inventario: {len(inventario)}")

# 5. Recorre la lista inventario con un bucle for.
print("\n--- Inventario Actual ---")
for producto in inventario:
    # Dentro del bucle, accede al nombre y al stock de ese diccionario e imprime un resumen.
    print(f"- {producto['nombre']}: {producto['stock']} unidades en stock.")
print ("\n--- Fin del Programa ---")
print ("Jhoel Ivan Macias Mamani")