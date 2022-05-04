import string
import pymongo
import pprint
from math import sin, cos, sqrt, atan2, radians
from pymongo import MongoClient, GEOSPHERE
from bson.son import SON
mongo_client = MongoClient(
    'mongodb+srv://dbUser:bCfuuaF1VFwjSyjA@cluster0.jms7j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = mongo_client.dummy_database  # assigning database to a variable


# funtion To insert dummy data
def insert_dummy_data():

    db.storesAgain.insert_many([{
    "title":"Store",
    "description":"Test Desecription",
    "location":{
        "type":"Point",
        "coordinates":[23.157101053251655,75.7999656402588]
    }
    },])
insert_dummy_data()

# db.storesAgain.create_index([("location", GEOSPHERE)])


# pipeline = [{"$project": {
#     "_id": 1,
#     "title": 1,
#     "loc":
#     {"type": "Point",
#         "coordinates": ["$latitude", "$longitude"]
#      }
# }
# }]

# pipeline2 = [{}]
# ans = list(db.storesAgain.find({"location": {"$geoWithin": {
#            "$centerSphere": [[26.2124, 78.1772], 1000/6371]}}}))
# print("ans", ans)


# ans = list(db.stores.aggregate(pipeline2))

# print(ans)

# # def is_inside(x1,y1,x2,y2):
# #     # approximate radius of earth in km
# #     R = 6373.0
# #     lat1 = radians(x1)
# #     lon1 = radians(y1)
# #     lat2 = radians(x2)
# #     lon2 = radians(y2)
# #     dlon = lon2 - lon1
# #     dlat = lat2 - lat1
# #     a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
# #     c = 2 * atan2(sqrt(a), sqrt(1 - a))
# #     distance = R * c
# #     # print("Result:", distance,"Km")
# #     return distance
# # # Traversing the records and checking
# # for store in db.stores.find({"title": "Store1"}):
# #   if is_inside(float(store['latitude']),float(store['longitude']),12,12) > 10:
# #       print("YES")


# # {
# #         "$match": {
# #             "title": {
# #                 "$eq":"Store1"
# #             },
# #             "loc": {"$geoWithin": {

# #                 "$centerSphere":[[22,22],5000000 / 3963.2]

# #             }}
# #         }
# #     }
