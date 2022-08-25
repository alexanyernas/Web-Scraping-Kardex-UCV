# Universidad Central de Venezuela
# Facultad de Ciencias
# Escuela de Computacion
# Asignatura: Lenguajes de Programacion (6204)
# Estudiantes:
#   Giannattasio Alejandra. V - 26.825.960
#   Naranjo Alexanyer.      V - 26.498.600

# https://github.com/py-pdf/PyPDF2
import PyPDF2
import re
# https://code.launchpad.net/beautifulsoup/
# from bs4 import BeautifulSoup

def getPdfData (nameFile):
    try:
        pdfFileObj  = open(f'./kardex/{nameFile}.pdf', 'rb')
        pdfReader   = PyPDF2.PdfFileReader(pdfFileObj)
        pagesText   = ''

        for i in range(pdfReader.numPages):
            pageObj    = pdfReader.getPage(i)
            pagesText  += f'\n{pageObj.extractText()}'

        pagesText             = pagesText.replace('_', '').split('\n')
        personalInformation   = pagesText[4:15]
        personalInformation   = personalInformation[:6] + [personalInformation[-1]]
        academyInformation    = pagesText[18:]
        academyInformationAux = []

        for item in academyInformation:
            if item.strip() != '':
                if item[0].isalpha():
                    itemAux = item.split(' ')
                    sizeAux = len(itemAux) - 1
                    if itemAux[sizeAux] in ['FINAL', 'REPARACION', '-']:
                        academyInformationAux.append(item)
                else:
                    academyInformationAux.append(item)

        asignatures = {}
        codePeriod  = ''

        for i in range(len(academyInformationAux)):
            asignatureAux = {}
            if academyInformationAux[i].strip() != '':
                if re.search('^(([0-9]+|(-)) (([0-9]+)|([A-Z]+))-([0-9]+))', academyInformationAux[i]):
                    codePeriod               = academyInformationAux[i].split(' ')[1]
                    asignatures[codePeriod]  = []
                    academyInformationAux[i] = ' '.join(academyInformationAux[i].split(' ')[2:])

                if re.search('(^([0-9]+)|(^-) (([0-9]+)|([A-Z]+))-([0-9]+))|(^[0-9]+)', academyInformationAux[i]):
                    if i == len(academyInformationAux) - 1:
                        actualAsignature = academyInformationAux[i].strip().split(' ')
                    elif i < len(academyInformationAux):
                        if not re.search('(^([0-9]+)|(^-) (([0-9]+)|([A-Z]+))-([0-9]+))|(^[0-9]+)', academyInformationAux[i+1]):
                            actualAsignature = f'{academyInformationAux[i]} {academyInformationAux[i+1]}'.strip().split(' ')
                            i += 1
                        else:
                            actualAsignature = academyInformationAux[i].strip().split(' ')

                    asignatureAux['code']   = actualAsignature[0]
                    if 'GRADO' in actualAsignature[-3]:
                        asignatureAux['uc'] = actualAsignature[-3].split('GRADO')[1]
                    else:    
                        asignatureAux['uc'] = actualAsignature[-3]
                    asignatureAux['note']   = actualAsignature[-2]
                    asignatureAux['method'] = actualAsignature[-1]
                    asignatures[codePeriod].append(asignatureAux)

        pdfFileObj.close()
        return personalInformation, asignatures

    except FileNotFoundError:
        print('File not found. Check the file name and try again.')
        return None