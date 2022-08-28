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
            print(f'\n- El estudiante {student.getFullName()} PUEDE graduarse.')
        else:
            print(f'\n- El estudiante {student.getFullName()}, NO PUEDE graduarse.')
            counterElectives, flagLab, flagCommunityService, flagInternship = student.getMissingAsignatures()
            if counterElectives < 10:
                print(f'- Falta por aprobar {10 - counterElectives} MATERIAS ELECTIVAS.')
            if not flagLab:
                print('- Laboratorio NO ha sido APROBADO.')
            if not flagCommunityService:
                print('- Servicio Comunitario NO ha sido APROBADO.')
            if not flagInternship:
                print('- Pasantías NO ha sido APROBADO.')