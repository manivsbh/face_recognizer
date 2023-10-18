from pymongo import MongoClient
import io
from detector import DEFAULT_ENCODINGS_PATH
from pathlib import Path
import face_recognition
import pickle

client = MongoClient("mongodb://localhost:27017/")
db = client.Images
images = db.Images_demo
encodings_location : Path = DEFAULT_ENCODINGS_PATH


def add_profile():
    global name
    global image_path
    data = input("Do you want to update your image in mongodb: ")
    if data == "Yes":
        image_path = input("Enter the path of the image ")
        name = input("Enter the name of the image ")
        with open(image_path, "rb") as file:
            image_bytes = io.BytesIO(file.read())
        image1 = {
            'name': name,
            'image': image_bytes.getvalue()
            }
        return images.insert_one(image1)
    if data == "No":
        exit()

def add_encodings():
    names1 = []
    encodings2 = []
    add_encode = input("Do you want to train the latest image ")
    if add_encode == "Yes":
       image_name = name 
       file_path = face_recognition.load_image_file(image_path)
       face_locations = face_recognition.face_locations(file_path)
       face_encodings = face_recognition.face_encodings(file_path, face_locations)
       for encoding in face_encodings:
            names1.append(image_name)
            encodings2.append(encoding)
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
           
       

