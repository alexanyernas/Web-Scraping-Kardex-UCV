# Universidad Central de Venezuela
# Facultad de Ciencias
# Escuela de Computacion
# Asignatura: Lenguajes de Programacion (6204)
# Estudiantes:
#   Giannattasio Alejandra. V - 26.825.960
#   Naranjo Alexanyer.      V - 26.498.600

# https://code.launchpad.net/beautifulsoup/
from bs4 import BeautifulSoup

def getDataPensum(year):

    def getDataAsignature(asignature):
        name    = asignature.find('h3').get_text()
        code    = asignature.find_all('p')[0].get_text().split(' ')[1]
        url     = asignature.find('a')['href']
        return {
            'code': code,
            'name': name,
            'url': url
        }

    file    = open("./Pensum/Pensum.html", encoding="utf8")
    scraper = BeautifulSoup(file, 'html.parser')

    result  = scraper.find(attrs={"id" : year})
    result  = result.find_all(attrs={"class" : "row"})

    auxResult = []
    for item in result:
        captions = item.find_all(attrs={"class" : "caption"})
        for caption in captions:
            auxResult.append(caption)

    asignatures = [] 
    for asignature in auxResult:
        asignatures.append(getDataAsignature(asignature))

    file.close()
    return asignatures