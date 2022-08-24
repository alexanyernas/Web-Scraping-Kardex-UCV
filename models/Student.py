# Universidad Central de Venezuela
# Facultad de Ciencias
# Escuela de Computacion
# Asignatura: Lenguajes de Programacion (6204)
# Estudiantes:
#   Giannattasio Alejandra. V - 26.825.960
#   Naranjo Alexanyer.      V - 26.498.600

class Student: 
    def __init__(self, degree, method, firstName, lastName, dni, email, notes, asignatures):
        self.degree      = degree
        self.method      = method
        self.firstName   = firstName
        self.lastName    = lastName
        self.dni         = dni
        self.email       = email
        self.notes       = notes
        self.asignatures = asignatures