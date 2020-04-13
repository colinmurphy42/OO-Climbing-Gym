# This is our main
import ClimbArea as ca


def main():
    # Creating climbing areas and adding them to area list
    areaList = [ca.BoulderArea("Cave", 15), ca.BigWallArea("Yosemite", 21), ca.BoulderArea("Comp", 9), ca.BigWallArea("Flat Iron", 12)]

    ondra = ca.RouteSetter(areaList)

    ondra.initAllRoutes()
    ondra.setNextRoute()
    ondra.setNextRoute()
    ondra.setNextRoute()
    ondra.setNextRoute()
    ondra.setNextRoute()


if __name__ == "__main__":
    main()
