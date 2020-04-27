class checkingIn:
    member = {}
    def __init__(self, mem):
        self.member = mem

    def getDescription(self): # the receipts
        return (self.member['name'] + "\nDailypass: $20")

    def gearcost(self): #cost for the add ons
        return 0

    def daypass(self): #cost of the daily entry
        if self.member['memType'] == 'Casual':
            return 20
        else:
            return 0
    def total(self): # puts them together for the Total
        if self.member['memType'] == 'Premium':
            return 0
        else:
            return self.gearcost() + self.daypass()

    def checkout(self): # returns the receipts object
        return ({'phone': self.member['phone'], 'desciption' : self.getDescription(), 'total' : self.total()})

# ===============================================================================================================
# Decorator
class GearDec(checkingIn):
    def __init__(self , phone):
        super().__init__(phone)

# ===============================================================================================================

class Shoes(GearDec):
    def __init__(self, checkingIn, phone):
        super().__init__(phone)
        self.tmp = checkingIn

    def getDescription(self):
        return self.tmp.getDescription() + "\nShoes: $3" #add to description

    def gearcost(self):
        return self.tmp.gearcost() + 3 #adds cost to gearcost



# ===============================================================================================================

class Harness(GearDec):
    def __init__(self, checkingIn, phone):
        super().__init__(phone)
        self.tmp = checkingIn

    def getDescription(self):
        return self.tmp.getDescription() + "\nHarness $4" #add to description

    def gearcost(self):
        return self.tmp.gearcost() + 4 #adds cost to gearcost

# ===============================================================================================================

class Rope(GearDec):
    def __init__(self, checkingIn, phone): 
        super().__init__(phone)
        self.tmp = checkingIn

    def getDescription(self):
        return self.tmp.getDescription() + "\nRope $5" #add to description

    def gearcost(self):
        return self.tmp.gearcost() + 5 #adds cost to gearcost
