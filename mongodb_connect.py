from pymongo import MongoClient
client = MongoClient('mongodb://10.255.11.171:27017/')
db = client.vto
cursor = db.test.find()
for document in cursor:
	print(document)