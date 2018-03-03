import pymongo
from pymongo import MongoClient
import pprint


class MongoOper():
    def __init__(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['myMongo']
        self.collection = db['bossType']

    def getTypeName(self):
        list = []
        for elem in self.collection.find():
            list.append(elem['name'])
        return list

    def getTypeUrl(self):
        list = []
        for elem in self.collection.find():
            list.append(elem['url'])
        return list

if __name__ == '__main__':
    a = MongoOper()
    print(a.getTypeName())
    print(a.getTypeUrl())