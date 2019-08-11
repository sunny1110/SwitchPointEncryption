import time
import services.data.mongo.mongoServices as mongoServices
import services.switchpoint.switchPointEncryption as switchPoint
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

frequency = int(config["PRESETS"]["frequency"])
db = config["PRESETS"]["db"]
collection = config["PRESETS"]["collection"]
username = config["PRESETS"]["username"]


def main():
    searchObj = {}
    searchObj["username"] = username
    userObject = mongoServices.getByKeyValue(db, collection, searchObj)
    decryptedPassword = switchPoint.newCrypt(userObject["password"], userObject["updated"])
    print(decryptedPassword)


if __name__ == '__main__':
    main()