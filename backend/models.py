from pymongo import MongoClient
from bson.objectid import ObjectId

class FoodItem:
    def __init__(self, name, image_url):
        self.name = name
        self.image_url = image_url

def get_food_items():
    db = get_database()
    collection = db["food_items"]
    return list(collection.find())

def add_food_item(name, image_url):
    db = get_database()
    collection = db["food_items"]
    food_item = {"name": name, "image_url": image_url}
    result = collection.insert_one(food_item)
    return str(result.inserted_id)

def update_food_item(item_id, name, image_url):
    db = get_database()
    collection = db["food_items"]
    result = collection.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": {"name": name, "image_url": image_url}}
    )
    return result.modified_count

def delete_food_item(item_id):
    db = get_database()
    collection = db["food_items"]
    result = collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count

