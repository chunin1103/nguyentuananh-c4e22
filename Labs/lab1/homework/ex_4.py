from matplotlib import pyplot
from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_default_database()

customer = db["customers"]
customers = customer.find()

reference = {
   "events": 0,
   "wom": 0,
   "ads": 0
}

for i in customers:
    if i["ref"]    == "events":
        reference["events"] += 1
    elif i["ref"]  == "wom":
        reference["wom"] += 1
    elif i["ref"]  == "ads":
        reference["ads"] += 1      

reference_count = (reference["events"], reference["wom"], reference["ads"]) 
reference_name = ["Events","Wom","Ads"] 

pyplot.pie(reference_count, labels = reference_name, autopct = "%0.2f%%", startangle = 90)
pyplot.title("Customers References")
pyplot.axis("equal")

pyplot.show()