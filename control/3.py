class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"


class Estudiante(Persona):
    def __init__(self, nombre, apellido, dni, legajo):
        super().__init__(nombre, apellido, dni)
        self.legajo = legajo

    def __str__(self):
        return f"{super().__str__()} - Legajo: {self.legajo}"


class Profesor(Persona):
    def __init__(self, nombre, apellido, dni, legajo, especialidad):
        super().__init__(nombre, apellido, dni)
        self.legajo = legajo
        self.especialidad = especialidad

    def __str__(self):
        return f"{super().__str__()} - Legajo: {self.legajo} - Especialidad: {self.especialidad}"


class Asignatura:
    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos

    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.creditos} créditos"


class Grupo:
    def __init__(self, numero, asignatura, profesor):
        self.numero = numero
        self.asignatura = asignatura
        self.profesor = profesor

    def __str__(self):
        return f"Grupo {self.numero} - {self.asignatura.nombre} - Profesor: {self.profesor.nombre} {self.profesor.apellido}"


class ProgramaAcademico:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre