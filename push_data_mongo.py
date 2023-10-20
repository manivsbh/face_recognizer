from pymongo import MongoClient
from pathlib import Path
from PIL import Image
import io
import os

client = MongoClient("mongodb://localhost:27017/")
db = client.Images
images = db.Images_demo

for filepath in Path("C:\\Users\\YashwanthSaiRamVanum\\Documents\\Local git\\face_recognizer\\training").glob("*/*"):
    name = filepath.parent.name
    with open(filepath, "rb") as file:
        image_bytes = io.BytesIO(file.read())
    image = {
    'name': name,
    'image': image_bytes.getvalue()
    }
    images.insert_one(image)

image_data = images.find_one({'name':"Elon musk"})
if image_data:
    image_find = image_data["image"]
    img = Image.open(io.BytesIO(image_find))
    img.show()
    
