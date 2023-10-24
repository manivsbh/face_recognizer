from pymongo import MongoClient
from pathlib import Path
from PIL import Image
import io
import os
from dotenv import load_dotenv


load_dotenv()

MONGODB_SERVER = os.getenv("MONGODB_SERVER")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

print(DATABASE_NAME)
print(COLLECTION_NAME)


client = MongoClient(MONGODB_SERVER) 
db = client.DATABASE_NAME  
images = db.COLLECTION_NAME 
for filepath in Path("C:\\Users\\YashwanthSaiRamVanum\\Documents\\Local git\\face_recognizer\\training").glob("*/*"):  
    name = filepath.parent.name
    with open(filepath, "rb") as file:
        image_bytes = io.BytesIO(file.read())
    image = {
    'name': name,
    'image': image_bytes.getvalue()
    }
    images.insert_one(image) 

# image_data = images.find_one({'name':"Elon musk"})
# if image_data:
#     image_find = image_data["image"]
#     img = Image.open(io.BytesIO(image_find))
#     img.show()
    
