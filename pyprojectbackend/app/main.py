from flask import Flask, g, jsonify, request
import pymongo
import pprint
import json
import time
from math import sin, cos, sqrt, atan2, radians
from pymongo import MongoClient
from flask_cors import CORS


mongo_client = MongoClient(
    'mongodb+srv://dbUser:bCfuuaF1VFwjSyjA@cluster0.jms7j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = mongo_client.dummy_database  # assigning database to a variable


app = Flask(__name__)
CORS(app)


def is_inside(x1, y1, x2, y2):
    # approximate radius of earth in km
    R = 6373.0
    lat1 = radians(x1)
    lon1 = radians(y1)
    lat2 = radians(x2)
    lon2 = radians(y2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    # print("Result:", distance,"Km")
    return distance


@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    return response


@app.route('/approach1', methods=['GET'])
def index():
    args = request.args
    radius = args.get("radius")
    latitude = args.get("lat")
    longitude = args.get("lng")
    if radius is None or latitude is None or longitude is None:
        return jsonify({"success": False, "message": "Please enter valid radius,lat and lng field in query"})
    # print(name)
    records = (db.storesAgain.find())
    ans = []
    for store in records:
        print(store)
        if is_inside(float(store['location']['coordinates'][0]), float(store['location']['coordinates'][1]), float(latitude), float(longitude)) <= int(radius):
            store['_id'] = str(store['_id'])
            ans.append(store)

    return jsonify({"data": ans})


@app.route('/approach2', methods=['GET'])
def index2():
    args = request.args
    radius = float(args.get("radius"))
    latitude = float(args.get("lat"))
    longitude = float(args.get("lng"))
    if radius is None or latitude is None or longitude is None:
        return jsonify({"success": False, "message": "Please enter valid radius,lat and lng field in query"})
    
    records = (db.storesAgain.find({"location": {"$geoWithin": {
        "$centerSphere": [[latitude,longitude], (radius)/6371]}}}))
    ans = []
    for store in records:
        store['_id'] = str(store['_id'])
        ans.append(store)

    return jsonify({"data": ans})
# python-project-sky