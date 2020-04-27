# Source:
# https://sourcemaking.com/design_patterns/object_pool/python/1

import DB, checkingIn, ClimbArea as ca
from datetime import tzinfo, timedelta, datetime


class OOGym:
    def __init__(self):
        self.db = DB.DB()
        self.dailyCust = []
        self.dbMem = None
        self.member = None
        self.gMember = None
        self.ondra = None

    # makes instance of checkingIn class and saves the customer object
    def checkIn(self, phone):
        self.dbMem = self.db.getMember(phone)
        self.member = checkingIn.checkingIn(self.dbMem)

    # the reciept that is added to know when the store opens
    def openRec(self):
        rec = {'date' : datetime.now()}
        rec.update({'phone' : 'Opening' , 'desciption' : 'Opening Time' , 'total' : -1})
        self.dailyCust.append(rec)

    # returns the customer reciept
    def showReceipt(self):
        return self.gMember.getDescription()

    # uses decorator to add gear
    def pickgear(self, shoes, rope , harness):
        self.gMember = self.member
        if (shoes == True):
            self.gMember = checkingIn.Shoes(self.gMember, self.member.member)
        if (rope == True):
            self.gMember = checkingIn.Rope(self.gMember, self.member.member)
        if (harness == True):
            self.gMember = checkingIn.Harness(self.gMember, self.member.member)

    # adds the datetime to reciept and adds it to daily customers list and set all save member info to None
    def checkOut(self):
        rec = {'date' : datetime.now()}
        rec.update(self.gMember.checkout())
        self.dailyCust.append(rec)
        self.dbMem = None
        self.member = None
        self.gMember = None
        return (rec)

    # adds the closing date and list of daily customer to DB
    def closing(self):
        data = {'date' : datetime.now() , 'dailyReceipts' : self.dailyCust}
        self.db.addRec(data)

    # adds new user to database
    def adduser(self, name, phone , M,C):
        exist = False
        cursor = self.db.coll()
        for i in cursor:   # makes sure user doesn't already exist
            if i['phone'] == phone:
                exist = True
        if exist == False:
            self.db.addUser(name, phone, M , C)
            return ("User: " + name + " added! :)")
        else:
            return ("Phone already exists")

    # changes the climber type
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
