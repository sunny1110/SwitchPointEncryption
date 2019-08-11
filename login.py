import services.data.mongo.mongoServices as mongoServices
import services.switchpoint.switchPointEncryption as switchPoint
from flask import Flask, request
app = Flask(__name__)
import json

config = configparser.ConfigParser()
config.read("settings.ini")

db = config["PRESETS"]["db"]
collection = config["PRESETS"]["collection"]

@app.route('/')
def welcome():
	return "<h1>Welcome to SwitchPoint Encrpytion</h1>"

@app.route('/login', methods = ["POST"])
def login():
    jsonForm = request.json
    username = jsonForm["username"]
    password = jsonForm["password"]
    searchObj = {}
    searchObj["username"] = username
    userObject = mongoServices.getByKeyValue(db, collection, searchObj)
    encryptedPassword = switchPoint.newCrypt(password, userObject["updated"])
    if(encryptedPassword==userObject["password"]):
        del userObject["_id"]
        return json.dumps(userObject)
    else:
        return "Failed Login!"