# Universidad Central de Venezuela
# Facultad de Ciencias
# Escuela de Computacion
# Asignatura: Lenguajes de Programacion (6204)
# Estudiantes:
#   Giannattasio Alejandra. V - 26.825.960
#   Naranjo Alexanyer.      V - 26.498.600

def processKardex(student):
    student.printPersonalInformation()
    student.printAcademicSummary()
    if student.isGaduate():
        print(f'\nEl/La Lic. {student.getFullName()}, ha visto {student.getTotalTimeOnSemester()} horas a lo largo de la carrera.\n')
    else:
        if student.canBeGraduated():
            print(f'\nEl estudiante {student.getFullName()} PUEDE graduarse.\n')
        else:
            print(f'\nEl estudiante {student.getFullName()}, NO PUEDE graduarse.\n')
            student.testingSoup()