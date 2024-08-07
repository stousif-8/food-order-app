from flask import Flask, jsonify, request
from models import get_food_items, add_food_item, update_food_item, delete_food_item
from database import get_database

app = Flask(__name__)

# Hardcoded food items
hardcoded_items = [
    {"name": "Pizza", "image_url": "https://images7.alphacoders.com/596/596343.jpg"},
    {"name": "Pasta", "image_url": "https://cdn.apartmenttherapy.info/image/fetch/f_auto,q_auto:eco/https://storage.googleapis.com/gen-atmedia/3/2018/12/a9696fb4dd17254516d5ebca8e3705ac7243dcfa.jpeg"},
    {"name": "Burger", "image_url": "https://brookrest.com/wp-content/uploads/2020/05/AdobeStock_282247995-scaled.jpeg"}
]

@app.route('/api/food-items', methods=['GET'])
def get_items():
    # Return hardcoded items instead of querying the database
    return jsonify(hardcoded_items)

@app.route('/api/food-items', methods=['POST'])
def create_item():
    data = request.json
    name = data.get('name')
    image_url = data.get('image_url')
    item_id = add_food_item(name, image_url)
    return jsonify({"id": item_id}), 201

@app.route('/api/food-items/<item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    name = data.get('name')
    image_url = data.get('image_url')
    updated_count = update_food_item(item_id, name, image_url)
    return jsonify({"modified_count": updated_count})

@app.route('/api/food-items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    deleted_count = delete_food_item(item_id)
    return jsonify({"deleted_count": deleted_count})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

