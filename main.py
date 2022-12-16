import string
from bs4 import BeautifulSoup
import webbrowser
import requests
from CarMake import CarMake

def getLinksOfCarMakes(url):
    print("Looking for data from ", url)
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    UnfilteredList = [a['href'] for a in soup.find_all('a', href=True)]
    filter1 = [x for x in UnfilteredList if "car-specs" in x]
    filter2 = [x for x in filter1 if "www" not in x]
    filter2.pop()
    print(filter2)
    return filter2

def getCarMakeNames(listOfCarMakes: list[string]) -> list[string]:
  return [x.split('/')[2] for x in listOfCarMakes]

def getLinksOfCarMakeModels(url, linksOfCarMakes):
    print("Looking for data from: ", url+linksOfCarMakes[0])
    result = requests.get(url+linksOfCarMakes[0])
    soup = BeautifulSoup(result.txt, "html.parser")
    print(soup)


url = "https://www.cars-directory.net/"
linksOfCarMakes = getLinksOfCarMakes(url)
numberOfCarMakes = len(linksOfCarMakes)
print(numberOfCarMakes)

listOfCarMakeNames = getCarMakeNames(linksOfCarMakes)
print(listOfCarMakeNames)

with open("FileToExport.txt", 'w') as f:
    for x in listOfCarMakeNames:
        f.write(x)
        f.write('\n')
    print("Data Exported")







