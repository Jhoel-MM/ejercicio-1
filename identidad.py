def es_identidad(matriz):
  # Requisito 1: Debe ser cuadrada
  num_filas = len(matriz)
  if num_filas == 0:
      return True  # Una matriz vacía es trivialmente identidad

  for i in range(num_filas):
      if len(matriz[i]) != num_filas:
          return False  # No es cuadrada

  # Requisito 2: Verificar la diagonal y los ceros
  for i in range(num_filas):
      for j in range(num_filas):
          if i == j:
              if matriz[i][j] != 1:
                  return False  # La diagonal no tiene 1
          else:
              if matriz[i][j] != 0:
                  return False  # Elemento fuera de la diagonal no es 0
  return True  # Cumple con todas las condiciones de matriz identidad

# Prueba tu función:
identidad = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
no_identidad = [[1, 0, 0], [0, 2, 0], [0, 0, 1]]
no_cuadrada = [[1, 0], [0, 1], [0, 0]]
assert es_identidad(identidad) == True
assert es_identidad(no_identidad) == False
assert es_identidad(no_cuadrada) == False
print ("todas las pruebas pasadas")