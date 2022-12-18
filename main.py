
import string
from bs4 import BeautifulSoup
import webbrowser
import requests
from CarMake import CarMake

# GRAB LINKS FROM URL + MAKE + MODEL 
def getLinks(url, forMake, forModel, listOfCarMakeLinks = None, listOfCarModelLinks = None):
    #Links for Make
    if forMake == True and forModel == False:
        global completedList
        print("Looking for data from: ", url, '\n')
        result = requests.get(url)
        completedList = bSParser(result, forModel)
    #Links for Model
    elif forMake == False and forModel == True:
        for index, make in enumerate(listOfCarMakeLinks):
            if index < 56:
                print("Looking for data from: ", url + make, '\n')
                result = requests.get(url + make)
                result = bSParser(result, forModel)
                completedList.extend(result)
            
    #Default 
    else:
        print("Looking for data from: ", url, '\n')
        result = requests.get(url)
    return completedList


def bSParser(result, forModel = None):
    soup = BeautifulSoup(result.text, "html.parser")
    List = [a['href'] for a in soup.find_all('a', href=True)]
    List = [x for x in List if "car-specs" in x]
    List = [x for x in List if "www" not in x]
    if forModel == True and bool(List) == True:
        List.pop(0)
    elif forModel == False and bool(List) == True:
        List.pop()
    return List

# EXTRACT CAR MODEL OR CAR MAKE FROM LINKS 
def extractFromLinks(listOfLinks, forMake, forModel = None):
    extractedList = []
    if forMake == True and forModel == False:
        forModel = True
        return [make.split('/')[2] for make in listOfLinks]

    elif forMake == False and forModel == True:
        return [model.split('/')[3] for model in listOfLinks]

#NEED A FUNCION THAT LOOP THROUGH THE ENTIRE LIST AND CALLS THE GET LINKS FUNCTION FOR EVERY CAR IN THE MAKE
def buildList(url, forMake, forModel, sizeOfCarMakes = None, listofCarMakes = None, listOfCarModels = None):
    #Get Links for CarMakes
    if forMake == True and forModel == False:
        linksOfCarMakes = getLinks(url, forMake, forModel)
        sizeOfCarMakes = len(linksOfCarMakes)
        forMake = False
        forModel = True
        return linksOfCarMakes, sizeOfCarMakes, forMake, forModel
    #Get Links for CarModel
    elif forMake == False and forModel == True:
        #Grab Links for Car Models
        linksForCarModels = getLinks(url, forMake, forModel, listofCarMakes)
        return linksForCarModels




forModel = False
forMake = True 
url = "https://www.cars-directory.net/"
sizeOfCarMakes = 0


#Build Inital list of carMakes + grab the Length of list
#linksOfCarMakes, sizeOfCarMakes, forMake, forModel = buildList(url, forMake, forModel)


#linksofCarModels = buildList(url, forMake, forModel, sizeOfCarMakes, linksOfCarMakes)
#print(*linksofCarModels, sep='\n')

myFile = open("FileToExport.txt", "r")
data = myFile.read()
data = data.split('\n')
print(type(data))
print(len(data))

linksOfMakes = data[:56]
#linksOfMakes = extractFromLinks(linksOfMakes, forMake,forModel)
#print(newData)

linksOfModels = data[55:1772]
forModel = True
forMake = False
print(*linksOfModels,sep='\n')
#print(len(linksOfModels))
#linksOfModels = extractFromLinks(linksOfModels, forMake,forModel)
#print(*linksOfModels,sep='\n')




#print(data)

with open("CarList.txt", 'w') as f:
    for make in linksOfMakes:
        #print(make.split('/')[2])
        f.write('\n')
        f.write(make.split('/')[2])
        f.write('\n')
        for model in linksOfModels:
            if  make.split('/')[2] == model.split('/')[2]:
                #print(model.split('/')[3])
                f.write(model.split('/')[3])
                f.write('\n')
   

    print("data exported")






