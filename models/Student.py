# Universidad Central de Venezuela
# Facultad de Ciencias
# Escuela de Computacion
# Asignatura: Lenguajes de Programacion (6204)
# Estudiantes:
#   Giannattasio Alejandra. V - 26.825.960
#   Naranjo Alexanyer.      V - 26.498.600

class Student: 
    def __init__(self, degree, method, lastName, firstName, dni, email, notes, asignatures):
        self.degree      = degree
        self.method      = method
        self.lastName    = lastName
        self.firstName   = firstName
        self.dni         = dni
        self.email       = email
        self.notes       = notes
        self.asignatures = asignatures
    
    def printPersonalInformation(self):
        print('\n\t:: PERSONAL INFORMATION ::')
        print(f'Degree:     {self.degree}')
        print(f'Method:     {self.method}')
        print(f'Last Name:  {self.lastName}')
        print(f'First Name: {self.firstName}')
        print(f'DNI:        {self.dni}')
        print(f'Email:      {self.email}')
    
    def printAcademicSummary(self):
        print('\n\t:: ACADEMIC SUMMARY ::')
        print(f'Credits:          {self.notes["creditos"]}')
        print(f'General Average:  {self.notes["promedioGeneral"]}')
        print(f'Approved Average: {self.notes["promedioAprobado"]}')
        print(f'Efficiency:       {self.notes["ponderadoEficiencia"]}')

    def isGaduate(self):
        for key in list(self.asignatures.keys())[::-1]:
            for asignature in self.asignatures[key]:
                if asignature['type'] == 'TEG':
                    if asignature['note'] == 'RET':
                        continue
                    if (asignature['note'] == 'A' or int(asignature['note']) > 10):
                        return True 
        return False

    def canBeGraduated(self):
        counterAsignatures       = 0
        seminarApproved          = False
        communityServiceApproved = False
        for key in list(self.asignatures.keys()):
            for asignature in self.asignatures[key]:
                if asignature['type'] == 'OBLIGATORIA':
                    if asignature['note'].isnumeric() and int(asignature['note']) > 10:
                        counterAsignatures += 1
                if asignature['type'] == 'SEMINARIO':
                    if asignature['note'].isnumeric() and int(asignature['note']) > 10:
                        seminarApproved = True
                if asignature['type'] == 'SERVICIO COMUNITARIO':
                    if asignature['note'] == 'A':
                        communityServiceApproved = True
        return counterAsignatures == 21 and seminarApproved and communityServiceApproved