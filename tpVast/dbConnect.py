from pymongo import MongoClient
import pymongo
from pymongo import MongoClient
from os import listdir
from os.path import isfile, join
import csv

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    #CONNECTION_STRING = "mongodb+srv://choineta:choineta123@InfovisVast.mongodb.net/myFirstDatabase"

    client = pymongo.MongoClient(
        "mongodb+srv://choineta:choineta123@infovisvast.ke6bo.mongodb.net/?retryWrites=true&w=majority")
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    #client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['Vast']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database

    path = 'media'
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    dbname = get_database()
    for i in range(5):
        fileName = onlyfiles[i]
        header = ["timestamp","currentLocation","participantId","currentMode","hungerStatus","sleepStatus","apartmentId","availableBalance","jobId","financialStatus","dailyFoodBudget","weeklyExtraBudget"]
        csvfile = open(path + '/' +fileName, 'r')
        reader = csv.DictReader(csvfile)
        print(fileName)
        for each in reader:
            row = {}
            for field in header:
                row[field] = each[field]

            #print(row)
            dbname.participantLog.insert_one(row)



