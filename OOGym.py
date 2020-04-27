import DB, checkingIn, ClimbArea as ca
from datetime import tzinfo, timedelta, datetime

class OOGym:
    def __init__(self):
        self.db = DB.DB()
        self.dailyCust = []
        self.dbMem = {'name' : ''}
        self.member = None
        self.gMember = None
        self.ondra = None

    def checkIn(self, phone): # Might add all chekcing in processes here to connect UI
        self.dbMem = self.db.getMember(phone)
        self.member = checkingIn.checkingIn(self.dbMem)

    def openRec(self):
        rec = {'date' : datetime.now()}
        rec.update({'phone' : 'Opening' , 'desciption' : 'Opening Time' , 'total' : -1})
        self.dailyCust.append(rec)

    def showReceipt(self):
        return self.gMember.getDescription()

    def pickgear(self, shoes, rope , harness):
        self.gMember = self.member
        if (shoes == True):
            self.gMember = checkingIn.Shoes(self.gMember, self.member.member)
        if (rope == True):
            self.gMember = checkingIn.Rope(self.gMember, self.member.member)
        if (harness == True):
            self.gMember = checkingIn.Harness(self.gMember, self.member.member)

    def checkOut(self):
        rec = {'date' : datetime.now()}
        rec.update(self.gMember.checkout())
        self.dailyCust.append(rec)
        self.member = None
        self.gMember = None
        return (rec)

    def closing(self):
        data = {'date' : datetime.now() , 'dailyReceipts' : self.dailyCust}
        self.db.addRec(data)

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

    def changeClimberType(self, phone, change):
        self.db.chgType(phone, change)

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
        #for a in self.ondra.areaList:
            #print(a.name, a.routes)
        self.ondra.addNewArea(ca.BoulderArea("Slab", 16))
