from pymongo import MongoClient
from pathlib import Path
from PIL import Image
import io
import os

client = MongoClient("mongodb://localhost:27017/")
db = client.face_recognization_inventory
images = db.image_name

for filepath in Path("/Users/manishcheepa/Documents/face_recognizer/face_recognizer/training").glob("*/*"):
    name = filepath.parent.name
    print(name)
    with open(filepath, "rb") as file:
        image_bytes = io.BytesIO(file.read())
    image = {
    'name': name,
    'image': image_bytes.getvalue()
    }
    images.insert_one(image)
    print("successfully inserted")

# image_data = images.find_one({'name':"juhi_singh"})
# if image_data:
#     image_find = image_data["image"]
#     img = Image.open(io.BytesIO(image_find))
#     img.show()
    
