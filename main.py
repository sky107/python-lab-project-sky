import pymongo
import pprint
from pymongo import MongoClient,GEO2D
from bson.son import SON
query = {"loc": SON([("$near", [3, 6]), ("$maxDistance", 100)])}
mongo_client = MongoClient('mongodb+srv://dbUser:bCfuuaF1VFwjSyjA@cluster0.jms7j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
# print(mongo_client)
print ("version:", pymongo.version)
db=mongo_client.geo_example
db.places.create_index([("loc", GEO2D)])
'loc_2d'
result = db.places.insert_many([{"loc": [2, 5]},
                                {"loc": [30, 5]},
                                {"loc": [1, 2]},
                                {"loc": [4, 4]}])

# for doc in db.places.find({"loc": {"$near": [3, 6]}}).limit(3):
#   pprint.pprint(doc)
for doc in db.places.find(query).limit(3):
  pprint.pprint(doc)
# https://pymongo.readthedocs.io/en/stable/examples/geo.html?highlight=geospatial#querying
