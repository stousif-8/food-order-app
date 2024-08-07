from pymongo import MongoClient

def get_database():
    client = MongoClient("mongodb://mongo:27017/")
    return client["food_order_db"]

