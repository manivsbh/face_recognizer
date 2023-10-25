from pymongo import MongoClient
import io
from detector import DEFAULT_ENCODINGS_PATH
from pathlib import Path
import face_recognition
import pickle
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_SERVER = os.getenv("MONGODB_SERVER")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")



client = MongoClient(MONGODB_SERVER)  
db = client[DATABASE_NAME]         
images = db[COLLECTION_NAME]   
encodings_location : Path = DEFAULT_ENCODINGS_PATH


def add_profile():
    global name
    global image_path
    data = input("Do you want to update your image in mongodb: ")
    if data == "yes":
        image_path = input("Enter the path of the image ")
        name = input("Enter the name of the image ")
        with open(image_path, "rb") as file:
            image_bytes = io.BytesIO(file.read())
        image_new = {
            'name': name,
            'image': image_bytes.getvalue()
            }
        return images.insert_one(image_new)
    if data == "no":
        exit()

def add_encodings():
    names_new = []
    encodings_new = []
    add_encode = input("Do you want to train the latest image ")
    if add_encode == "yes":
       image_name = name 
       file_path = face_recognition.load_image_file(image_path)
       face_locations = face_recognition.face_locations(file_path)
       face_encodings = face_recognition.face_encodings(file_path, face_locations)
       for encoding in face_encodings:
            names_new.append(image_name)
            encodings_new.append(encoding)
    #    name_encodings1 = {"names": names, "encodings": encodings}
       print(encoding)

       with open(encodings_location, 'rb') as file:
           existing_data = pickle.load(file)
           print(existing_data)
           existing_data["names"].append(image_name)
           existing_data["encodings"].append(encoding)

    #    for obj in existing_data:
        

       

    #    existing_data.update(name_encodings1)

       with open(encodings_location, 'wb') as f:
           pickle.dump(existing_data, f)
       exit()
    if add_encode == "No":
        exit()
           
       

