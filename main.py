# Universidad Central de Venezuela
# Facultad de Ciencias
# Escuela de Computacion
# Asignatura: Lenguajes de Programacion (6204)
# Estudiantes:
#   Giannattasio Alejandra. V - 26.825.960
#   Naranjo Alexanyer.      V - 26.498.600

import sys
from helpers.getPdfData import getPdfData
from models.Student import Student

nameFile = sys.argv[1]
result   = getPdfData(nameFile)

if result:
    personalInformation, asignatures                       = result
    degree, method, lastName, firstName, dni, email, notes = personalInformation
    notes    = notes.split(' ')
    notesAux = {
        'creditos'           : notes[0],
        'promedioGeneral'    : notes[1],
        'promedioAprobado'   : notes[2],
        'ponderadoEficiencia': notes[3]
    }
    student = Student(degree, method, lastName, firstName, dni, email, notesAux, asignatures)
    #student.printPersonalInformation()
    #student.printAcademicSummary()
    #print(asignatures)
    if not student.isGaduate():
        print(student.canBeGraduated())