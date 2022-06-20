import pymongo
from pymongo import MongoClient
"""mongodb+srv://admin:<password>@cluster0.ogibm.mongodb.net/?retryWrites=true&w=majority"""

cluster = MongoClient("mongodb+srv://admin:admin123@cluster0.ogibm.mongodb.net/?retryWrites=true&w=majority")

db = cluster["sldb"]
collection = db["employee"]

post = {"name": "Changappa", "email":"chang@abcd.com"}

collection.insert_one(post)