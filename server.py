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


    while(True):
        searchObj = {}
        searchObj["username"] = username
        userObject = mongoServices.getByKeyValue(db, collection, searchObj)
        print(userObject)
        encryptObject = switchPoint.reCrypt(userObject["password"], userObject["updated"])
        # print(userObject)
        # print("\n")
        # print(encryptObject)
        mongoServices.updateField(db, collection, searchObj, encryptObject)
        print("Encrypted @{}: {}".format(encryptObject["updated"], encryptObject["password"]))

        time.sleep(frequency)



if __name__ == '__main__':


    main()

