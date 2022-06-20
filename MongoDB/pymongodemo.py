import pymongo
from pymongo import MongoClient
"""mongodb+srv://admin:<password>@cluster0.ogibm.mongodb.net/?retryWrites=true&w=majority"""

cluster = MongoClient("mongodb+srv://admin:admin123@cluster0.ogibm.mongodb.net/?retryWrites=true&w=majority")

db = cluster["sldb"]
collection = db["employee"]

post1 = {"name": "Changappa", "email":"chang@abcd.com"}
post2 = {"name": "Changappa2", "email":"chang2@abcd.com"}


collection.insert_many([post1, post2])