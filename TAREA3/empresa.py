class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def describir_rol(self):
        print("Soy un empleado de esta empresa.")



class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento

    def describir_rol(self):
        print("Soy un gerente.")
        print(f"Estoy a cargo del departamento de {self.departamento}.")


class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, especialidad):
        super().__init__(nombre, edad, salario)
        self.especialidad = especialidad

    def describir_rol(self):
        print("Soy un ingeniero.")
        print(f"Mi especialidad es {self.especialidad}.")


class Asistente(Empleado):
    def __init__(self, nombre, edad, salario, jefe):
        super().__init__(nombre, edad, salario)
        self.jefe = jefe

    def describir_rol(self):
        print("Soy un asistente.")
        print(f"Soy el asistente de {self.jefe}.")


empleado1 = Gerente("Valentin", 20, 59000, "Marketing")
empleado2 = Ingeniero("Simon", 22, 4500, "Desarrollo")
empleado3 = Asistente("Nicolas", 21, 3000, "valentin")

print(empleado1.describir_rol())
print(empleado2.describir_rol())
print(empleado3.describir_rol())