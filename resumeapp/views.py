from resumeapp import app
from flask import request, render_template
from pymongo import MongoClient
import json
from bson import json_util


def database_connection():
    #returns database connection
    connect = MongoClient("127.0.0.1", 27017)
    database = connect.cv
    return database


def get_Json(data):
    #converts data to JSON format
    return json.dumps(data, default=json_util.default)


@app.route('/api', methods=['GET'])
def json_data():
    if request.method == 'GET':
        data_holder = []
        db_results = database_connection().users.find()
    for result in db_results:
        data_holder.append(result)
    return get_Json(data_holder)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html", data=json_data)





