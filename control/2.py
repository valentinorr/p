class libro:
  def __init__(self, titulo, autor, anio):
    self.titulo = titulo
    self.autor = autor
    self.anio = anio

class libreria:
  def __init__(self):
    self.libro = []

  def add_libro(self, libro):
    self.libro.append(libro)

  def libro_por_titulo(self, titulo):
    for libro in self.libro:
      if libro.titulo == titulo:
        return libro
    return None

libreria = libreria()

libreria.add_libro(libro("harry potter", "Roberto Carlos ", 1210))
libreria.add_libro(libro("The Hobbit", "J.R.R. Tolkien", 1982))
libreria.add_libro(libro("Historias extraordinarias", "Edgar Allan Poe", 1846))

libro = libreria.libro_por_titulo("Historias extraordinarias")

if libro is not None:
  print(libro.titulo)
  print(libro.autor)
  print(libro.anio)
else:
  print("el libro no se encuentra.")