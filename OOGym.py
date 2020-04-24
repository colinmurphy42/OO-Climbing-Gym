import DB, checkingIn, ClimbArea

class OOGym:
    def __init__():
        self.db = DB.DB()
        self.dailyCust = []


    #def checkIn(phone): # Might add all chekcing in processes here to connect UI
    #pass

    #     memObj = self.db.getMember(phone)
    #     checkObj = checkingIn.checkingIn(memObj)
    # if (shoes == True):
    #     checkObj = checkingIn.Shoes(checkObj, memObj)
    # if (Rope == True):
    #     checkObj = checkingIn.Rope(checkObj, memObj)
    # if (Harness == True):
    #     checkObj = checkingIn.Harness(checkObj, memObj)
    #
    # rec = {'date' : datetime.now() - timedelta(hours=7)}
    # rec.update(checkObj.checkout())
    # self.dailyCust.append(rec)
    # return (rec)


    def addGear(mem):
        pass

    def closing():
        data = {'date' : datetime.now() - timedelta(hours=7) , 'dailyReceipts' : self.dailyCust}

    def adduser(self, name, phone , M,C):
        self.db.addUser(name, phone, M , C)
        return ("User: " + name + " added! :)")
