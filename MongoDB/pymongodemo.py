import pymongo
from pymongo import MongoClient
"""mongodb+srv://admin:<password>@cluster0.ogibm.mongodb.net/?retryWrites=true&w=majority"""

cluster = MongoClient("mongodb+srv://admin:admin123@cluster0.ogibm.mongodb.net/?retryWrites=true&w=majority")

db = cluster["sldb"]
collection = db["employee"]

post1 = {"_id": 101,"name": "Changappa", "email":"chang@abcd.com"}
post2 = {"_id": 102,"name": "Changappa2", "email":"chang2@abcd.com"}


# collection.insert_many([post1, post2])

# results = collection.find_one({"name": "Changappa"})
# print(results["email"])

# for result in results:
#     print(result["email"])

# results= collection.delete_many({"name" : "Changappa"})
collection.update_one({"_id": 102}, {"$set" : {"name": "Changappa123"}})