import DB, checkingIn, ClimbArea as ca

class OOGym:
    def __init__(self):
        self.db = DB.DB()
        self.dailyCust = []
        self.dbMem = None
        self.ondra = None

    def checkIn(self, phone): # Might add all chekcing in processes here to connect UI
        self.dbMem = self.db.getMember(phone)
        self.member = checkingIn.checkingIn(self.dbMem)

    def pickgear():
        if (shoes == True):
            self.member = checkingIn.Shoes(checkObj, memObj)
        if (Rope == True):
            self.member = checkingIn.Rope(checkObj, memObj)
        if (Harness == True):
            self.member = checkingIn.Harness(checkObj, memObj)

    def checkOut():
        rec = {'date' : datetime.now() - timedelta(hours=7)}
        rec.update(self.member.checkout())
        self.dailyCust.append(rec)
        return (rec)

    def closing():
        data = {'date' : datetime.now() - timedelta(hours=7) , 'dailyReceipts' : self.dailyCust}

    def adduser(self, name, phone , M,C):
        exist = False
        cursor = self.db.coll()
        for i in cursor:
            if i['phone'] == phone:
                exist = True
        if exist == False:
            self.db.addUser(name, phone, M , C)
            return ("User: " + name + " added! :)")
        else:
            return ("Phone already exists")

    def establishRoutes(self):
        # Creating climbing areas and adding them to area list
        areaList = [ca.BoulderArea("Cave", 15), ca.BigWallArea("Yosemite", 16), ca.BoulderArea("Comp", 9),
                    ca.BigWallArea("Flat Iron", 12)]
        # Our route setter
        self.ondra = ca.RouteSetter(areaList)
        self.ondra.initAllRoutes()
        #for i in range(9):
        #    ondra.setNextRoute()
        # Areas will be part of the setter class after they are initialized
        for a in self.ondra.areaList:
            print(a.name, a.routes)
        self.ondra.addNewArea(ca.BoulderArea("Slab", 16))

