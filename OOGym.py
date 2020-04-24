import DB, checkingIn, ClimbArea

class OOGym:
    def __init__(self):
        self.db = DB.DB()
        self.dailyCust = []
        self.dbMem = None

    def checkIn(self, phone): # Might add all chekcing in processes here to connect UI
        self.dbMem = self.db.getMember(phone)
        self.member = checkingIn.checkingIn(self.dbMem)

    def pickgear(self, shoes, rope , harness):
        if (shoes == True):
            self.member = checkingIn.Shoes(self.member, self.member.member)
        if (rope == True):
            self.member = checkingIn.Rope(self.member, self.member.member)
        if (harness == True):
            self.member = checkingIn.Harness(self.member, self.member.member)

    def checkOut():
        rec = {'date' : datetime.now() - timedelta(hours=7)}
        rec.update(self.member.checkout())
        self.dailyCust.append(rec)
        self.member = None
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
