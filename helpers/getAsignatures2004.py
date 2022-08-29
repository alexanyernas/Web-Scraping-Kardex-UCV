# Universidad Central de Venezuela
# Facultad de Ciencias
# Escuela de Computacion
# Asignatura: Lenguajes de Programacion (6204)
# Estudiantes:
#   Giannattasio Alejandra. V - 26.825.960
#   Naranjo Alexanyer.      V - 26.498.600

# https://code.launchpad.net/beautifulsoup/
from bs4 import BeautifulSoup

def getAsignatures2004():

    def hasAttrBgColor(tag):
        return tag.has_attr('bgcolor') 

    file    = open("./Pensum/2004.html", encoding="utf8")
    scraper = BeautifulSoup(file, 'html.parser')

    result  = scraper.find_all('tbody')[1]
    result  = result.find_all(hasAttrBgColor)

    asignatures = {}

    for item in result:
        auxResult = item.find_all('td') 
        auxResult = auxResult[1:len(auxResult) - 5]

        auxAsignature = []
        for value in auxResult:
            if '(*)' in value.get_text():
                auxAsignature.append(value.get_text()[4:])
            else:    
                auxAsignature.append(value.get_text())

        asignatures[auxAsignature[0]] = auxAsignature[1:]

    file.close()

    aux = asignatures['6109']
    del asignatures['6109']
    asignatures['6105'] = aux
    
    return asignatures