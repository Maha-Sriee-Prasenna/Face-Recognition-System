import cv2
import os
import pickle
import face_recognition
import numpy as np
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import numpy as np
from datetime import datetime

cred = credentials.Certificate("faceapp\serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceappforhealth-default-rtdb.firebaseio.com/",
    'storageBucket':"faceappforhealth.appspot.com"
})
bucket = storage.bucket()

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBack = cv2.imread('faceapp/interface/back.png')


modepath = os.listdir('faceapp/interface')
modelist = ['faceapp/interface/' + i for i in modepath]
# print(modelist)
# print(modepath)

file = open("Encodings.p",'rb')
encodelistwithknownames = pickle.load(file)
file.close()
know,imgnames = encodelistwithknownames
#print(imgnames)

modetype = 0
counter = 0
id =-1
imgperson =[]

print("file is loading")
while True:
    s, img = cap.read()

    imgBack[120:120+480, 70:70+640] = img
    imgs =cv2.resize(img,(0,0),None,0.25,0.25)
    imgs = cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)

    fcurrentf = face_recognition.face_locations(imgs)
    ecurrentf=face_recognition.face_encodings(imgs,fcurrentf)

    imgBack[15:15+670,810:810+450]= cv2.imread(modelist[modetype])

    if fcurrentf :
        for enface , faceloc in zip(ecurrentf,fcurrentf):
            matches = face_recognition.compare_faces(know,enface)
            facedis = face_recognition.face_distance(know,enface)
            #print("match:",matches)
            #print("facedis:",facedis)
            matchIndex = np.argmin(facedis)

            if matches[matchIndex]:
                #print("know face is detected: ",imgnames[matchIndex])
                y1,x2,y2,x1=faceloc
                y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                bbox =90+x1,170+y1,x2-x1,y2-y1
                imgBack = cvzone.cornerRect(imgBack,bbox,rt = 0)
                id = imgnames[matchIndex]
                # print(id)
                # info = db.reference("Details/"+id).get()
                # print(info)
                if counter == 0:
                    cvzone.putTextRect(imgBack,"loading",(275,400))
                    cv2.imshow("face attendition", imgBack)
                    cv2.waitKey(1)
                    counter = 1
                    modetype = 1


        if counter != 0:
            if counter == 1:
                info = db.reference("Details/"+id).get()
                print(info)
                blob  = bucket.get_blob(id+".jpeg")
                array = np.frombuffer(blob.download_as_string(),np.uint8)
                imgperson = cv2.imdecode(array,cv2.COLOR_BGRA2BGR)

                date_time = datetime.strptime(info['last attend'],"%Y-%m-%d %H:%M:%S")
                sec = (datetime.now() - date_time).total_seconds()
                
                if sec > 30:
                    ref = db.reference("Details/"+id)
                    info["attend"]+=1
                    ref.child("attend").set(info['attend'])
                    ref.child("last attend").set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    modetype=3
                    counter=0
                    imgBack[15:15+670,810:810+450]= cv2.imread(modelist[modetype])

            if modetype!=3:

                if 10<counter<20:
                    modetype = 2 

                imgBack[15:15+670,810:810+450]= cv2.imread(modelist[modetype])

                if counter<=10:
                    (w,h),_ =cv2.getTextSize(info['name'],cv2.FONT_HERSHEY_COMPLEX_SMALL,1,1)
                    offset = (252-w)//2
                    cv2.putText(imgBack,str(info['name']),(975+offset,350),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),1)
                    cv2.putText(imgBack,str(info['age']),(1080,417),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),1)
                    cv2.putText(imgBack,str(info['attend']),(970,530),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
                    cv2.putText(imgBack,str(info['year']),(1147,530),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)

                    imgBack[86:86+216,917:917+216] = imgperson
                    cv2.waitKey(5)

                counter +=1

                if counter>=20:
                    counter = 0
                    modetype = 0
                    info =[]
                    imgperson =[]
                    imgBack[15:15+670,810:810+450]= cv2.imread(modelist[modetype])

    else:
        modetype =0
        counter = 0

    cv2.imshow("webcam", img)
    cv2.imshow("face attendition", imgBack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

