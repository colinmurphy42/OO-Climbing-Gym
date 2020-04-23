import pymongo
from pymongo import MongoClient
from datetime import tzinfo, timedelta, datetime

class DB:
    def __init__(self):
        self.__CONNECTION_STRING = "mongodb+srv://oscardel13:ahOv9313@ooclimbinggym-pdhjh.mongodb.net/test?retryWrites=true&w=majority"
        client = pymongo.MongoClient(self.__CONNECTION_STRING)
        db = client.get_database('OOClimbingGym')
        self._collection = db['Gym1']
        self._Receipts = db['Receipts']

    # returns the members object
    def getMember(self, phone):
        return self._collection.find_one({'phone' : phone})

    # Changes members climbing type
    def chgType(self, phone, change):
        past = self._collection.find_one({'phone' : phone})['climbType']
        self._collection.update({'phone' : phone}, {'$set' : {'climbType' : change}})
        now = self._collection.find_one({'phone' : phone})['climbType']
        print("changed Climbers type from: " + past + " to : " + now)

    # Changes members membership
    def chgMem(self):
        past = self._collection.find_one({'phone' : phone})['memType']
        self._collection.update({'phone' : phone}, {'$set' : {'memType' : change}})
        now = self._collection.find_one({'phone' : phone})['memType']
        print("changed membership from: " + past + " to : " + now)

    # adds new member to database
    def addUser(self, name, mem, climb, phone):
        data = {'name' : name}
        data.update({'memType' : mem})
        data.update({'climbType' : climb})
        data.update({'phone' : phone})
        data.update({'waiver' : True})
        self._collection.insert_one(data)
        print("added")

    # adds receipt to database
    def addRec(self, phone , desc, total):
        data = {'date' : datetime.now() - timedelta(hours=7)}
        data.update({'phone' : phone})
        data.update({'desciption' : desc})
        data.update({'total' : total})
        self._Receipts.insert_one(data)
        print("Added Receipt")
