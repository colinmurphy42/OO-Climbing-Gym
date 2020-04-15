# This is our main
import ClimbArea as ca


def main():
    # Creating climbing areas and adding them to area list
    areaList = [ca.BoulderArea("Cave", 15), ca.BigWallArea("Yosemite", 21), ca.BoulderArea("Comp", 9),
                ca.BigWallArea("Flat Iron", 12)]
    # Our route setter
    ondra = ca.RouteSetter(areaList)
    ondra.initAllRoutes()
    for i in range(9):
        ondra.setNextRoute()
    # Areas will be part of the setter class after they are initialized
    for a in ondra.areaList:
        print(a.name, a.routes)

    ondra.addNewArea(ca.BoulderArea("Slab", 16))
    for a in ondra.areaList:
        print(a.name, a.routes)

if __name__ == "__main__":
    main()
