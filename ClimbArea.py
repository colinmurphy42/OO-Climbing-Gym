from SettingBehavior import SettingBoulder
from SettingBehavior import SettingBigWall


class ClimbArea(object):
    def __init__(self, setStrategy, name, wallSize):
        self.setStrategy = setStrategy
        self.name = name
        self.wallSize = wallSize
        self.routes = []

    # Change the routes
    def setRoutes(self, wallSize):
        return self.setStrategy.setRoutes(wallSize)

    # Retrieve current routes
    def getRoutes(self):
        return self.routes


class BoulderArea(ClimbArea):
    def __init__(self, name, wallSize):
        self.grades = ["V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10", "V11"]
        super(BoulderArea, self).__init__(SettingBoulder(self.grades), name, wallSize)


class BigWallArea(ClimbArea):
    def __init__(self, name, wallSize):
        self.grades = ["5.6", "5.7", "5.8", "5.9", "5.10", "5.11", "5.12", "5.13", "5.14", "5.15"]
        super(BigWallArea, self).__init__(SettingBigWall(self.grades), name, wallSize)


# Route-setter to handle the changing of routes
class RouteSetter(object):
    def __init__(self, areaList):
        self.areaList = areaList
        self.areaCounter = 0

    # This is used to remember what area needs new routes next
    def increaseCounter(self):
        self.areaCounter += 1
        if self.areaCounter >= len(self.areaList):
            self.areaCounter = 0

    def initAllRoutes(self):
        # Gives all the areas routes
        print("Setting all routes")
        for area in self.areaList:
            area.routes = area.setRoutes(area.wallSize)
            print(area.name, "now has these routes:", area.routes)

    def setNextRoute(self):
        # Get the next area and change its routes
        nextArea = self.areaList[self.areaCounter]
        print("Setting ", nextArea.name)
        self.areaList[self.areaCounter].routes = nextArea.setRoutes(nextArea.wallSize)
        # This is for documentation of changes
        print("New routes: ", self.areaList[self.areaCounter].routes)
        # Increase counter
        self.increaseCounter()

    def addNewArea(self, area):
        # Check if the parameter is correct
        if isinstance(area, BoulderArea) or isinstance(area, BigWallArea):
            # Initialize some routes
            area.routes = area.setRoutes(area.wallSize)
            # Append it to area list
            self.areaList.append(area)
        else:
            print("Area was not inputted correctly")