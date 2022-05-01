import string
import pymongo
import pprint
from math import sin, cos, sqrt, atan2, radians
from pymongo import MongoClient,GEO2D
from bson.son import SON
mongo_client = MongoClient('mongodb+srv://dbUser:bCfuuaF1VFwjSyjA@cluster0.jms7j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db=mongo_client.dummy_database # assigning database to a variable


# funtion To insert dummy data
# def insert_dummy_data():
  
#     db.stores.insert_many([{
#     "title":"Store",
#     "description":"Test Desecription",
#     "latitude":"23.157101053251655",
#     "longitude":"75.7999656402588"
#     },])
# insert_dummy_data()
# db.places.create_index([("loc", GEO2D)])
pipeline = [{"$project":{
    "_id":1,
    "title":1,
    "loc":
    {   "type":"Point",
        "coordinates":["$latitude","$longitude"]
    }
},
}, {
        "$match": {
            "title": {
                "$eq":"Store" 
            },
            "loc": {"$geoWithin": {

                "$centerSphere":["loc.coordinates",5 / 3963.2]

            }}
        }
    }]
ans=list(db.stores.aggregate(pipeline))

print(ans)

# def is_inside(x1,y1,x2,y2):
#     # approximate radius of earth in km
#     R = 6373.0
#     lat1 = radians(x1)
#     lon1 = radians(y1)
#     lat2 = radians(x2)
#     lon2 = radians(y2)
#     dlon = lon2 - lon1
#     dlat = lat2 - lat1
#     a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1 - a))
#     distance = R * c
#     # print("Result:", distance,"Km")
#     return distance
# # Traversing the records and checking
# for store in db.stores.find({"title": "Store1"}):
#   if is_inside(float(store['latitude']),float(store['longitude']),12,12) > 10:
#       print("YES")





  

