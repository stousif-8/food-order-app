from pymongo import MongoClient

def get_database():
    client = MongoClient("mongodb+srv://admin:admin@my-app.5zs8j.mongodb.net/?retryWrites=true&w=majority&appName=my-app/tousif")
    return client["food_order_db"]

