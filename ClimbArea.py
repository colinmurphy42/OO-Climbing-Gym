from SettingBehavior import SettingBoulder
from SettingBehavior import SettingBigWall


class ClimbArea(object):
    def __init__(self, setStrategy, name, wallSize):
        self.setStrategy = setStrategy
        self.name = name
        self.wallSize = wallSize
        self.routes = []

    def setRoutes(self, wallSize):
        return self.setStrategy.setRoutes(wallSize)


class BoulderArea(ClimbArea):
    def __init__(self, name, wallSize):
        super(BoulderArea, self).__init__(SettingBoulder(), name, wallSize)


class BigWallArea(ClimbArea):
    def __init__(self, name, wallSize):
        super(BigWallArea, self).__init__(SettingBigWall(), name, wallSize)


# Route-setter to handle the changing of routes
class RouteSetter(object):
    def __init__(self, areaList):
        self.areaList = areaList
        self.areaCounter = 0

    def increaseCounter(self):
        self.areaCounter += 1
        if self.areaCounter >= len(self.areaList):
            self.areaCounter = 0

    def initAllRoutes(self):
        print("Setting all routes")
        for area in self.areaList:
            area.routes = area.setRoutes(area.wallSize)
            print(area.name, "now has these routes:", area.routes)

    def setNextRoute(self):
        #Get the next area to change route
        nextArea = self.areaList[self.areaCounter]
        print("Setting next route:")
        print(nextArea.setRoutes(nextArea.wallSize), nextArea.name)
        self.increaseCounter()

