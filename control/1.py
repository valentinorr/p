def busqueda_binaria(arreglo, objetivo):
  inicio = 0
  final = len(arreglo) - 1

  while inicio <= final:
    medio = (inicio + final) // 2

    if arreglo[medio] == objetivo:
      return medio
    elif arreglo[medio] < objetivo:
      inicio = medio + 1
    else:
      final = medio - 1

  return -1