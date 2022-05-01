import string
import pymongo
import pprint


from pymongo import MongoClient
mongo_client = MongoClient('mongodb+srv://dbUser:bCfuuaF1VFwjSyjA@cluster0.jms7j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db=mongo_client.dummy_database # assigning database to a variable


# funtion To insert dummy data
def insert_dummy_data():
    db.stores.insert_many([{
    "title":"Store1",
    "description":"Test Desecription",
    "latitude":"12.32",
    "longitude":"12.53"
    }])

insert_dummy_data()




# Traversing the records and checking
for store in db.stores.find({"title": "Store1"}):





# approximate radius of earth in km


  

