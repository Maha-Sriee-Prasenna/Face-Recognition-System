import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("faceapp\serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceappforhealth-default-rtdb.firebaseio.com/"
})

ref = db.reference('Details')

data ={
        "Elon Musk":{
        "name":"Elon Musk",
        "age":55,
        "year":1969,
        "last attend":"2023-02-19 00:55:55",
        "attend":7
    },
        "Chris":{
        "name":"Chris hemisworth",
        "age":50,
        "year":1974,
        "last attend":"2023-10-01 00:55:55",
        "attend":7
    }
}

for key,val in data.items():
    ref.child(key).set(val)