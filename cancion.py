# 1. Crear una lista vacía llamada biblioteca_musical
biblioteca_musical = []

# 2. Crear al menos tres diccionarios diferentes, cada uno representando una canción
cancion1 = {
    "titulo": "Be More",
    "artista": "Stephen Sanchez",
    "album": "Angel Face",
    "duracion_segundos": 210,
    "genero": "pop-Rock",
    "año_publicacion": 2023,
    "es_sencillo": False,
    "colaboraciones": []
}

cancion2 = {
    "titulo": "As It Was",
    "artista": "Harry Styles",
    "album": "Harry's House",
    "duracion_segundos": 167,
    "genero": "Pop",
    "año_publicacion": 2022,
    "es_sencillo": True,
    "colaboraciones": []
}

cancion3 = {
    "titulo": "dime",
    "artista": "kevin kaarl",
    "album": "ultra sodade",
    "duracion_segundos": 203,
    "genero": "folk",
    "año_publicacion": 2025,
    "es_sencillo": True,
    "colaboraciones": []
}

# 3. Añadir cada diccionario a la lista biblioteca_musical
biblioteca_musical.append(cancion1)
biblioteca_musical.append(cancion2)
biblioteca_musical.append(cancion3)

# 4. Imprimir la cantidad de canciones en la biblioteca
print(f"Cantidad de canciones en la biblioteca: {len(biblioteca_musical)}")

# 5. Recorrer la lista y mostrar título y artista de cada canción
print("\n--- Biblioteca Musical ---")
for cancion in biblioteca_musical:
    print(f"- '{cancion['titulo']}' por {cancion['artista']}")
print("\n fin del programa")
print("Jhoel Ivan Macias Mamani")
