class Reserva:
    def __init__(self, nombre, numero, fecha):
        self.nombre_del_pasajero = nombre
        self.numero_de_vuelo = numero
        self.fecha = fecha

    def mostrar_detalle(self):
        pass

class ReservaEconomica(Reserva):
    def mostrar_detalle(self):
        print(f"Reserva económica para {self.nombre_del_pasajero} en el vuelo {self.numero_de_vuelo} el {self.fecha}.")

class ReservaBusiness(Reserva):
    def mostrar_detalle(self):
        print(f"Reserva business para {self.nombre_del_pasajero} en el vuelo {self.numero_de_vuelo} el {self.fecha}.")

class ReservaPrimeraClase(Reserva):
    def mostrar_detalle(self):
        print(f"Reserva de primera clase para {self.nombre_del_pasajero} en el vuelo {self.numero_de_vuelo} el {self.fecha}.")

if __name__ == "__main__":
    reserva1 = ReservaEconomica("Amaro", 123, "2023-10-15")
    reserva2 = ReservaBusiness("Nicolas", 777, "2023-11-20")
    reserva3 = ReservaPrimeraClase("Rodolfo", 666, "2023-12-25")

    reserva1.mostrar_detalle()
    reserva2.mostrar_detalle()
    reserva3.mostrar_detalle()
