class checkingIn:
    member = {}
    def __init__(self, mem):
        self.member = mem

    def getDescription(self):
        return (self.member['name'] + "\nDailypass: $20")

    def gearcost(self):
        return 0

    def daypass(self):
        if self.member['memType'] == 'Casual':
            return 20
        else:
            return 0
    def total(self):
        if self.member['memType'] == 'Premium':
            return 0
        else:
            return self.gearcost() + self.daypass()

    def checkout(self):
        return ({'phone': self.member['phone'], 'desciption' : self.getDescription(), 'total' : self.total()})

# ===============================================================================================================

class GearDec(checkingIn):
    def __init__(self , phone):
        super().__init__(phone)

# ===============================================================================================================

class Shoes(GearDec):
    def __init__(self, checkingIn, phone):
        super().__init__(phone)
        self.tmp = checkingIn

    def getDescription(self):
        return self.tmp.getDescription() + "\nShoes: $3"

    def gearcost(self):
        return self.tmp.gearcost() + 3

    def daypass(self):
        return self.tmp.daypass()

# ===============================================================================================================

class Harness(GearDec):
    def __init__(self, checkingIn, phone):
        super().__init__(phone)
        self.tmp = checkingIn

    def getDescription(self):
        return self.tmp.getDescription() + "\nHarness $4"

    def gearcost(self):
        return self.tmp.gearcost() + 4

    def daypass(self):
        return self.tmp.daypass()

# ===============================================================================================================

class Rope(GearDec):
    def __init__(self, checkingIn, phone):
        super().__init__(phone)
        self.tmp = checkingIn

    def getDescription(self):
        return self.tmp.getDescription() + "\nRope $5"

    def gearcost(self):
        return self.tmp.gearcost() + 5

    def daypass(self):
        return self.tmp.daypass()
