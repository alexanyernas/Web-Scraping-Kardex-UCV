from bs4 import BeautifulSoup

def getDataAsignature(asignature):
    name = asignature.find('h3').get_text()
    code = asignature.find_all('p')[0].get_text().split(' ')[1]
    url = asignature.find('a')['href']
    return {
        'code': code,
        'name': name,
        'url': url
    }

file = open("./Pensum/Pensum.html", encoding="utf8")
scraper = BeautifulSoup(file, 'html.parser')

result = scraper.find(attrs={"id" : "1974"})
result = result.find_all(attrs={"class" : "row"})

auxResult = []
for item in result:
    captions = item.find_all(attrs={"class" : "caption"})
    for caption in captions:
        auxResult.append(caption)

asignatures = [] 
for asignature in auxResult:
    asignatures.append(getDataAsignature(asignature))

file.close()