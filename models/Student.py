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
    
    def printPersonalInformation(self):
        print('\n\t:: PERSONAL INFORMATION ::')
        print(f'Degree:     {self.degree}')
        print(f'Method:     {self.method}')
        print(f'First Name: {self.firstName}')
        print(f'Last Name:  {self.lastName}')
        print(f'DNI:        {self.dni}')
        print(f'Email:      {self.email}')
    
    def printAcademicSummary(self):
        print('\n\t:: ACADEMIC SUMMARY ::')
        print(f'Credits:          {self.notes["creditos"]}')
        print(f'Approved Average: {self.notes["promedioAprobado"]}')
        print(f'General Average:  {self.notes["promedioGeneral"]}')
        print(f'Efficiency:       {self.notes["ponderadoEficiencia"]}')
