import pymongo
client = pymongo.MongoClient("mongodb+srv://RuluyiSwuro:tvvbvrkvvarmm@cluster0.izs9si1.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "Ruluyi",
    "email" : "ruluyi@ineuron.ai",
    "surname" : "Swuro"

}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)