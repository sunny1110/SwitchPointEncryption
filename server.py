import time
import services.data.mongo.mongoServices as mongoServices
import services.switchpoint.switchPointEncryption as switchPoint

frequency = 5
db = "switchpoint"
collection = "users"
username = "prithvi.prakash@gmail.com"

def main():
    while(True):
        searchObj = {}
        searchObj["username"] = username
        userObject = mongoServices.getByKeyValue(db, collection, searchObj)
        encryptObject = switchPoint.reCrypt(userObject["password"], userObject["updated"])
        # print(userObject)
        # print("\n")
        # print(encryptObject)
        mongoServices.updateField(db, collection, searchObj, encryptObject)
        print("Encrypted at {}".format(encryptObject["updated"]))
        time.sleep(frequency)



if __name__ == '__main__':
    main()

