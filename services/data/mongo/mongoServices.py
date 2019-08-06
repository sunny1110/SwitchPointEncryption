from pymongo import MongoClient
import time

def connectToCollection(db, collection):
    try:
        client = MongoClient()
        dbCon = client[db]
        return dbCon[collection]
    except Exception as e:
        print("The following exception has occured in connectToCollection: {}".format(e))

def setCounterField(collection, object, colCon):
    try:
        counter = colCon.find().count()
        object[collection+"Id"] = counter+1
        return object
    except Exception as e:
        print("The following exception has occured in setCounterField: {}".format(e))


def addToCollection(db, collection, object):
    try:
        colCon = connectToCollection(db, collection)
        counterObject = setCounterField(collection, object, colCon)
        colCon.insert_one(counterObject)
        print("Inserted Object to Collection: {} of Database: {}".format(collection, db))
    except Exception as e:
        print("The following exception has occured in addToCollection: {}".format(e))


def getByKeyValue(db, collection, searchCritera):
    try:
        colCon = connectToCollection(db, collection)
        searchObject = colCon.find_one(searchCritera)
        return searchObject
    except Exception as e:
        print("The following exception has occured in getByKeyValue: {}".format(e))

def updateField(db, collection, searchCritera, updatedField):
    try:
        colCon = connectToCollection(db, collection)
        updateStatement = {"$set": updatedField}
        colCon.update_one(searchCritera, updateStatement)
    except Exception as e:
        print("The following exception has occured in updateField: {}".format(e))

def main():

    insertObj = {"username": "jack.com", "password": "******"}
    addToCollection("switchpoint", "users", insertObj)
    # searchObj = {"lastName": "Colback"}
    # updateObj = {"lastName": "Dorsey"}
    # # so = getByKeyValue("python", "start", searchObj)
    # # print(so)
    # updateField("python", "start",searchObj, updateObj)


if __name__ == '__main__':
    main()
