# Source:
# https://sourcemaking.com/design_patterns/object_pool/python/1

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

    def checkIn(self, phone): # Might add all checking in processes here to connect UI
        self.dbMem = self.db.getMember(phone)
        self.member = checkingIn.checkingIn(self.dbMem)

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

    def closing():
        data = {'date' : datetime.now() , 'dailyReceipts' : self.dailyCust}

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

    # This function initializes the gyms routes and route setter
    def establishRoutes(self):
        # Creating climbing areas and adding them to area list
        areaList = [ca.BoulderArea("Cave", 15), ca.BigWallArea("Yosemite", 16), ca.BoulderArea("Comp", 9),
                    ca.BigWallArea("Flat Iron", 12)]

        # Our route setter
        self.ondra = ca.RouteSetter(areaList)
        self.ondra.initAllRoutes()
        self.ondra.addNewArea(ca.BoulderArea("Slab", 16))

# Object Pool Pattern Here:
class ticketPool:
    def __init__(self, poolSize):
        self.tickets = []
        # Make an array of ticket objects as large as the pool size
        for i in range(poolSize):
            self.tickets.append(Ticket(i))
        #self._tickets = [Ticket() for _ in range(poolSize)]

    # Retrieving a ticket
    def getTicket(self):
        if len(self.tickets) == 0:
            print("No more tickets")
            return None
        return self.tickets.pop()

    # Returning a ticket
    def releaseTicket(self, ticket):
        self.tickets.append(ticket)

# Ticker objects to keep track of capacity
class Ticket:
    def __init__(self, ticketNum):
        # Make an array of ticket objects as large as the pool size
        self.ticketNumber = ticketNum + 1
