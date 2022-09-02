# Universidad Central de Venezuela
# Facultad de Ciencias
# Escuela de Computacion
# Asignatura: Lenguajes de Programacion (6204)
# Estudiantes:
#   Giannattasio Alejandra. V - 26.825.960
#   Naranjo Alexanyer.      V - 26.498.600

from helpers.getDataPensum import getDataPensum
from helpers.getAsignatures2004 import getAsignatures2004

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

    def getFullName(self):
        return f'{self.lastName} {self.firstName}'
    
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
        print(f'Efficiency:       {self.notes["ponderadoEficiencia"]}\n')

    def isGaduate(self):
        for key in list(self.asignatures.keys())[::-1]:
            for asignature in self.asignatures[key]:
                if asignature['type'] == 'TEG':
                    if asignature['note'] == 'RET':
                        continue
                    if (asignature['note'] == 'A' or int(asignature['note']) >= 10):
                        return True 
        return False

    def canBeGraduated(self):
        counterAsignatures       = 0
        seminarApproved          = False
        communityServiceApproved = False
        for key in list(self.asignatures.keys()):
            for asignature in self.asignatures[key]:
                if asignature['type'] == 'OBLIGATORIA':
                    if asignature['note'].isnumeric() and int(asignature['note']) >= 10:
                        counterAsignatures += 1
                    if asignature['note'] == 'EQ':
                        counterAsignatures += 1
                if asignature['type'] == 'SEMINARIO':
                    if asignature['note'].isnumeric() and int(asignature['note']) >= 10:
                        seminarApproved = True
                if asignature['type'] == 'SERVICIO COMUNITARIO':
                    if asignature['note'] == 'A':
                        communityServiceApproved = True
        return counterAsignatures == 21 and seminarApproved and communityServiceApproved
    
    def getTotalTimeOnSemester(self):
        counterTime = 0
        for key in list(self.asignatures.keys()):
            for asignature in self.asignatures[key]:
                if asignature['note'].isnumeric():
                    if int(asignature['note']) >= 10:
                        counterTime += (int(asignature['uc']))
                else:
                    if asignature['note'] == 'A' or asignature['note'] == 'EQ': 
                        counterTime += (int(asignature['uc']))
        return counterTime * 15
    
    def getAprovedObligatoriesAsignatures(self):
        def isObligatorieAproved(asignature):
            if (asignature['type'] == 'OBLIGATORIA'):

                if asignature['code'] == '6105' or asignature['code'] == '6109':
                    if asignature['note'].isnumeric():
                        if int(asignature['note']) >= 10:
                            return True
                    else:
                        if asignature['note'] == 'EQ':
                            return True
                    return False

                if asignature['note'].isnumeric():
                    if int(asignature['note']) >= 10:
                        return True
                else:
                    if asignature['note'] == 'EQ':
                        return True
            return False
        result = []
        for key in list(self.asignatures.keys()):
            for asignature in self.asignatures[key]:
                if isObligatorieAproved(asignature):
                    result.append(asignature)
        return result

    def getMissingAsignatures(self):
        counterElectives     = 0
        flagLab              = False
        flagCommunityService = False
        flagInternship       = False
        asignatures2004      = getAsignatures2004()
        aprovedAsignatures   = self.getAprovedObligatoriesAsignatures()

        for asignature in aprovedAsignatures:
            if asignature['code'] == '6105':
                del asignatures2004['6109']
            if asignature['code'] in asignatures2004.keys():
                del asignatures2004[asignature['code']]

        for key in list(self.asignatures.keys()):
            for asignature in self.asignatures[key]:
                if asignature['type'] == 'ELECTIVA':
                    if asignature['note'].isnumeric():
                        if int(asignature['note']) >= 10:
                            counterElectives += 1
                    else:
                        if asignature['note'] == 'A':
                            counterElectives += 1
                
                if asignature['type'] == 'PASANTIA':
                    if asignature['note'].isnumeric():
                        if int(asignature['note']) >= 10:
                            flagInternship = True
                    else:
                        if asignature['note'] == 'A':
                            flagInternship = True
                
                if asignature['type'] == 'SERVICIO COMUNITARIO':
                    if asignature['note'] == 'A':
                        flagCommunityService = True
                
                if asignature['type'] == 'LABORATORIO':
                    if asignature['note'] == 'A':
                        flagLab = True
        
        return counterElectives, flagLab, flagCommunityService, flagInternship, asignatures2004
    
    def getPdfAsignatures(self):
        print('\t:: PDF LIST ::')
        for key in list(self.asignatures.keys()):
            year = int(key.split('-')[1])
            if year >= 2000:
                year = 2000
                pensum = getDataPensum('2000')
            elif year >= 1985 and year <= 1999:
                year = 1985
                pensum = getDataPensum('1985')
            elif year >= 1974 and year <= 1984:
                year = 1974
                pensum = getDataPensum('1974')
            elif year >= 1968 and year <= 1973:
                year = 1968
                pensum = getDataPensum('1968')
            
            for asignature in self.asignatures[key]:
                found = False
                for item in pensum:
                    if asignature['code'] == item['code']:
                        
                        if asignature['type'] == 'OBLIGATORIA':
                            if asignature['note'].isnumeric():
                                if int(asignature['note']) >= 10:
                                    auxItem = item
                            else:
                                if asignature['note'] == 'EQ':
                                    auxItem = item

                        if asignature['type'] == 'ELECTIVA':
                            if asignature['note'].isnumeric():
                                if int(asignature['note']) >= 10:
                                    auxItem = item
                            else:
                                if asignature['note'] == 'A':
                                    auxItem = item
                        
                        if asignature['type'] == 'LABORATORIO':
                            if asignature['note'] == 'A':
                                auxItem = item
                        
                        print(f'* {auxItem["code"]}')
                        print(f'* {auxItem["name"]}')
                        print(f'* {auxItem["url"]}')
                        print(f'* Año de PENSUM: {year}\n')
                        found = True
                        break
                    
                if asignature['note'].isnumeric():
                    if int(asignature['note']) >= 10:
                        if not found:
                            print(f'- Materia {asignature["code"]}, NO SE ENCUENTRA en el sitio web de computación.\n')
                elif asignature['note'] == 'A':
                        if not found:
                            print(f'- Materia {asignature["code"]}, NO SE ENCUENTRA en el sitio web de computación.\n')
                elif asignature['note'] == 'EQ':
                        if not found:
                            print(f'- Materia {asignature["code"]}, NO SE ENCUENTRA en el sitio web de computación.\n')