from pymongo import MongoClient
con = MongoClient("mongodb://localhost:27017")
db = con['crud']
col = db['intern']
print("connect")
