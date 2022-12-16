
class CarMake():
    def __init__(self, makeName, numberOfCarsProduced):

        class CarModel():
            def __init__(self, model, year, engineconfig, horsepower):
                self.model = model
                self.year = year
                self.engineconfig = engineconfig
                self.horsepower = horsepower

            def printSpecs(self):
                print("This is the ", self.year,
                      ", " + self.model + ". It has a  " + self.engineconfig + " that produces ",
                      self.horsepower, " horsepower!")
