from pymongo import MongoClient
import os

def get_connection():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    client = MongoClient(mongo_uri)
    return client["Thesis"]

def load_charging_sessions(collection_name, filter_dict=None, limit=None):
    db = get_connection()
    collection = db[collection_name]
    if filter_dict:
        query = filter_dict
    else:
        query = {}
    cursor = collection.find(query)
    if limit:
        cursor = cursor.limit(limit)
    return list(cursor)