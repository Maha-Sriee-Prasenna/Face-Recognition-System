import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("faceapp\serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceappforhealth-default-rtdb.firebaseio.com/",
    'storageBucket':"faceappforhealth.appspot.com"
})

imgdir ='faceapp/img/'
imgpath = os.listdir(imgdir)

imglist = [imgdir + i for i in imgpath]

imgnames = []

for filename in imgpath:
    base_name = filename.rsplit('.', 1)[0]
    imgnames.append(base_name)

    fileName=f'{imgdir}{filename}'
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.upload_from_filename(fileName)

# Print the resulting lists
print("Image Paths:", imglist)
print("Image Names:", imgnames)

#print(imgnames)

def findEncoding(images):
    encodelist = []
    for img in images:
        img = cv2.imread(img)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encodes = face_recognition.face_encodings(img)[0]
        encodelist.append(encodes);
    return encodelist


print("encode started")
know =findEncoding(imglist)
encodelistwithknownames = [know,imgnames]
#print(know)
print("encode complete")

file = open("Encodings.p",'wb')
pickle.dump(encodelistwithknownames,file)
file.close()
print("file saved")