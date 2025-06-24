producto = {
    "codigo": "P001",
    "nombre": "Chocolate para Taza 'El Ceibo'",
    "precio_unitario": 15.50,
    "stock": 50,
    "proveedor": "El cecibo Ltda."
}
print(f"Producto: {producto['nombre']} - Precio: Bs. {producto['precio_unitario']:.2f}")

unidades_vendidas = 5
producto['stock'] -= unidades_vendidas
print(f"Stock actualizado despues de la venta: {producto['stock']} unidades")

producto['en_oferta'] = True

print("\nDiccionario completo del producto con todos los cambios:")
print(producto)