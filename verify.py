import time
import services.data.mongo.mongoServices as mongoServices
import services.switchpoint.switchPointEncryption as switchPoint

frequency = 5
db = "switchpoint"
collection = "users"
username = "prithvi.prakash@gmail.com"

def main():
    searchObj = {}
    searchObj["username"] = username
    userObject = mongoServices.getByKeyValue(db, collection, searchObj)
    decryptedPassword = switchPoint.newCrypt(userObject["password"], userObject["updated"])
    print(decryptedPassword)


if __name__ == '__main__':
    main()