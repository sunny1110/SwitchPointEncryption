import services.data.mongo.mongoServices as mongoClient
import services.switchpoint.switchPointEncryption as switchPoint
import time
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

db = config["PRESETS"]["db"]
collection = config["PRESETS"]["collection"]

def main():
    username = input("Please enter username: ")
    password = input("Please enter password: ")
    created = int(time.time())
    updated = int(time.time())
    encryptedPassword = switchPoint.newCrypt(password, updated)
    userObject = {}
    userObject["username"] = username
    userObject["password"] = encryptedPassword
    userObject["created"] = created
    userObject["updated"] = updated
    mongoClient.addToCollection(db, collection, userObject)


if __name__ == '__main__':
    main()