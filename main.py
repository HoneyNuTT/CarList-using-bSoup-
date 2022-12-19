
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
    #Links for Year of Models
    elif forMake == False and forModel == False:
        print('Links for Year of Models')
        for idx, make in enumerate(listOfCarMakeLinks):
            if idx < 56:
                for index, model in enumerate(listOfCarModelLinks[57:1772]):
                    if make.split('/')[2] == model.split('/')[2]:
                        print("Looking for data from: ", url + make + model.split('/')[3], '\n')
                        result = requests.get(url + make + model.split('/')[3])
                        result = bSParser(result, forMake, forModel)
                        completedList.extend(result)
    #Default 
    else:
        print("Looking for data from: ", url, '\n')
        result = requests.get(url)
    return completedList


def bSParser(result, forMake = None, forModel = None):
    if forMake == False and forModel == False:
        soup = BeautifulSoup(result.text, "html.parser")
        List = [a['href'] for a in soup.find_all('a', href=True)]
        List = [x for x in List if "car-specs" in x]
        List = [x for x in List if "www" not in x]
        List.pop(0)
        List.pop(0)
        return List
        
    else:
        soup = BeautifulSoup(result.text, "html.parser")
        List = [a['href'] for a in soup.find_all('a', href=True)]
        List = [x for x in List if "car-specs" in x]
        List = [x for x in List if "www" not in x]
   
        if forMake == True and bool(List) == True:
            List.pop(0)
        elif forModel == True and bool(List) == True:
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
def buildList(url, forMake, forModel, sizeOfCarMakes = None, linksOfCarMakes = None, linksOfCarModels = None):
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
        linksOfCarModels = getLinks(url, forMake, forModel, linksOfCarMakes)
        forMake = False
        forModel = False
        return linksOfCarModels, forMake, forModel
         
    elif forMake == False and forModel == False:
        return getLinks(url, forMake, forModel, linksOfCarMakes, linksOfCarModels)



forMake = True 
forModel = False

url = "https://www.cars-directory.net/"
sizeOfCarMakes = 0


#Build Inital list of carMakes + grab the Length of list
linksOfCarMakes, sizeOfCarMakes, forMake, forModel = buildList(url, forMake, forModel)

linksOfCarModels, forMake, forModel = buildList(url, forMake, forModel, sizeOfCarMakes, linksOfCarMakes)

#print(forMake)
#print(forModel)
#print(*linksOfCarModels, sep='\n')

linksOfCarYears = buildList(url, forMake, forModel, sizeOfCarMakes, linksOfCarMakes, linksOfCarModels,)

#myFile = open("FileToExport.txt", "r")
#data = myFile.read()



#linksOfMakes = e#linksOfMakes = data[:56]xtractFromLinks(linksOfMakes, forMake,forModel)
#print(newData)

#linksOfModels = data[55:1772]
#print(*linksOfModels,sep='\n')
#print(len(linksOfModels))
#linksOfModels = extractFromLinks(linksOfModels, forMake,forModel)
#print(*linksOfModels,sep='\n')

with open('TestFile.txt','w') as f:
    for x in linksOfCarYears:
        f.write(x)
        f.write('\n')
    print("data exported")



#with open("CarList.txt", 'w') as f:
#    for make in linksOfMakes:
#        f.write('\n')
#        f.write(make.split('/')[2])
#        f.write('\n')
#        for model in linksOfModels:
#            if  make.split('/')[2] == model.split('/')[2]:
#                f.write(model.split('/')[3])
#                f.write('\n')
#    print("data exported")






