class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Matricula: {self.matricula}")


class Profesor(Persona):
    def __init__(self, nombre, edad, codigo_empleado):
        super().__init__(nombre, edad)
        self.codigo_empleado = codigo_empleado

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Código de empleado: {self.codigo_empleado}")


class Asignatura:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def mostrar_info(self):
        print(f"Asignatura: {self.nombre}")
        print(f"Código: {self.codigo}")


class Grupo:
    def __init__(self, numero, asignatura):
        self.numero = numero
        self.asignatura = asignatura

    def mostrar_info(self):
        print(f"Grupo número: {self.numero}")
        self.asignatura.mostrar_info()


class ProgramaAcademico:
    def __init__(self, nombre, codigo, asignaturas):
        self.nombre = nombre
        self.codigo = codigo
        self.asignaturas = asignaturas

    def mostrar_info(self):
        print(f"Programa académico: {self.nombre}")
        print(f"Código: {self.codigo}")
        print("Asignaturas:")
        for asignatura in self.asignaturas:
            asignatura.mostrar_info()

asignatura1 = Asignatura("Matemáticas", "MAT1")
asignatura2 = Asignatura("Física", "FIS10")
grupo1 = Grupo(1, asignatura1)
grupo2 = Grupo(2, asignatura2)
asignaturas_programa = [asignatura1, asignatura2]
programa_academico = ProgramaAcademico("Ingeniería", "ING101", asignaturas_programa)
estudiante = Estudiante("Valentin", 20, "E12345")
profesor = Profesor("Elliot", 25, "P98765")

print("Información del estudiante:")
estudiante.mostrar_info()

print("\nInformación del profesor:")
profesor.mostrar_info()

print("\nInformación del grupo 1:")
grupo1.mostrar_info()

print("\nInformación del programa académico:")
programa_academico.mostrar_info()
