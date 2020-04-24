import checkingIn
import DB
import GymGUI
import ClimbArea as ca

def main():
    '''
    # OSCAR WORK
    db = DB.DB()
    member = db.getMember("1234")
    test = checkingIn.checkingIn(member)
    test = checkingIn.Shoes(test, member)
    test = checkingIn.Rope(test, member)
    test = checkingIn.Harness(test, member)

    print(test.member)
    print(test.getDescription() + " for a total: " + str(test.total()))
    '''
    #THIS RUNS GUI
    app = GymGUI.gymGUI()
    app.mainloop()

    # # test.checkout()
    #
    # # Creating climbing areas and adding them to area list
    # areaList = [ca.BoulderArea("Cave", 15), ca.BigWallArea("Yosemite", 21), ca.BoulderArea("Comp", 9),
    #             ca.BigWallArea("Flat Iron", 12)]
    # # Our route setter
    # ondra = ca.RouteSetter(areaList)
    # ondra.initAllRoutes()
    # for i in range(9):
    #     ondra.setNextRoute()
    # # Areas will be part of the setter class after they are initialized
    # for a in ondra.areaList:
    #     print(a.name, a.routes)
    # ondra.addNewArea(ca.BoulderArea("Slab", 16))
    # for a in ondra.areaList:
    #     print(a.name, a.routes)

if __name__ == "__main__":
    main()
