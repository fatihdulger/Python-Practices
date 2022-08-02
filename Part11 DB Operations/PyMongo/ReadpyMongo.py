from pprint import pprint
from pymongo import MongoClient # import mongo client
from pymongo import MongoClient


# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb+srv://fatihdulger:XXXXXXXXXX(need mongoDB password here).ivd1jne.mongodb.net/test')
filter={}

result = client['c10DB']['myCol'].find(
  filter=filter
)

"variable = connectionVariable [DatabaseName] [CollectionName]"

result = client['c10DB']['myCol']

"""for members in result.find():

    # pprint(members)

    print(members)"""



# rerieve and prints one document

query1 = result.find_one(

    {

        "MemberID": 17,

    }

)

print(query1)



# retrieve fom another collection in the same database

print("from testCol collection\n")

result1 = client['c10DB']['myCol']

query2 = result.find_one({"restaurant_id": "40356151"})

print(query2)



# result2 = client["sample_training"]["grades"]

# for studentGrades in result.find():

#     pprint(studentGrades)

