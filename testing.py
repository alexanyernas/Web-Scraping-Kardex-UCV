from bs4 import BeautifulSoup

def hasAttrBgColor(tag):
    return tag.has_attr('bgcolor') 

file = open("./Pensum/2004.html", encoding="utf8")
scraper = BeautifulSoup(file, 'html.parser')

result = scraper.find_all('tbody')[1]
result = result.find_all(hasAttrBgColor)

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

print(asignatures)

file.close()
    # if item.find('a'):
    #     auxResult = item.find('a')
    #     print(auxResult['href'])