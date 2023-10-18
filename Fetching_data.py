from pymongo import MongoClient
import io
from PIL import Image
import face_recognition
import urllib.request as ur

client = MongoClient("mongodb://localhost:27017/")
db = client.Images
images = db.Images_demo
print("Name")


# for filepath in db.images.find():
#         name = filepath["name"]
#         image = Image.open(io.BytesIO(filepath["image"]))
#         print(name)
names = []
encodings = []
model = "hog"
# encodings_location = DEFAULT_ENCODINGS_PATH

for doc in images.find():
    print (doc["name"])
    # image = Image.open(io.BytesIO(doc["image"]))
    # print(doc["image"])
    # image.show()
    image_bytes = io.BytesIO(doc["image"])

    # You can access the image data using image_bytes.getvalue()
    # image_data = image_bytes.getvalue()
    name = doc["name"]
    image = face_recognition.load_image_file(image_bytes)
        # print(name)
    face_locations = face_recognition.face_locations(image, model=model)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    for encoding in face_encodings:
        names.append(name)
        encodings.append(encoding)

    name_encodings = {"names": names, "encodings": encodings}
    print(name_encodings)
    # with encodings_location.open(mode="wb") as f:
    #     pickle.dump(name_encodings, f)