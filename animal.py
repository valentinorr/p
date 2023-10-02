class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print(f"El perro {self.nombre} ladra.")

class Gato(Animal):
    def sonido(self):
        print(f"El gato {self.nombre} maúlla.")

class Pajaro(Animal):
    def sonido(self):
        print(f"El pájaro {self.nombre} canta.")

if __name__ == "__main__":
    miPerro = Perro("rofolfo", 3)
    miGato = Gato("Garfield", 5)
    miPajaro = Pajaro("chimuelo", 2)

    miPerro.sonido()
    miGato.sonido()
    miPajaro.sonido()
