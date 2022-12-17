import string
from bs4 import BeautifulSoup
import webbrowser
import requests
from CarMake import CarMake

# GRAB LINKS FROM URL + MAKE + MODEL 
def getLinks():
    if isMake == True:
        print("Looking for data from: ", url+linksOfCarMakes[0])
        result = requests.get(url+linksOfCarMakes[0])
    else:
        print("Looking for data from: ", url)
        result = requests.get(url)

    soup = BeautifulSoup(result.text, "html.parser")
    List = [a['href'] for a in soup.find_all('a', href=True)]
    List = [x for x in List if "car-specs" in x]
    List = [x for x in List if "www" not in x]
    List.pop()

    if isModel == True:
        List.pop(0)

    return List

# EXTRACT CAR MODEL OR CAR MAKE FROM LINKS 
def extractFromLinks(listOfLinks, isModel: list[string]) -> list[string]:
    if isModel == True:
         return [x.split('/')[2] for x in listOfLinks]
    elif isModel == False:
        return [x.split('/')[3] for x in listOfLinks]



#NEED A FUNCION THAT LOOP THROUGH THE ENTIRE LIST AND CALLS THE GET LINKS FUNCTION FOR EVERY CAR IN THE MAKE
def buildListFromLinks():
    if isMake == False and isModel == False:
        global linksOfCarMakes
        linksOfCarMakes = getLinks()
        print(*linksOfCarMakes, sep='\n')
        isMake = True





global url
global isModel
global isMake
isModel = False
isMake = False 
url = "https://www.cars-directory.net/"


buildListFromLinks()




#with open("FileToExport.txt", 'w') as f:
 #   for x in listOfCarMakeNames:
  #      f.write(x)
   #     f.write('\n')
   # print("Data Exported")






