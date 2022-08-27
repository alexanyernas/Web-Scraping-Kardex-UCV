# import re
import re
from bs4 import BeautifulSoup

def hasAttrBgColor(tag):
    return tag.has_attr('bgcolor') 

file = open("./Pensum/2004.html", encoding="utf8")
scraper = BeautifulSoup(file, 'html.parser')
result = scraper.find_all(hasAttrBgColor)
result = result[1].find_all('td')
urlAux = result[-1]
print(result)
print(urlAux.find('a'))
for item in result:
    print(item.get_text())
# temp = result[0].replace('<td>', ' ')
# temp = temp.replace('</td>', ' ')
# print(temp)