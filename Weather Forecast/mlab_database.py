from crawl_accuweather import date
from pymongo import MongoClient
uri = "mongodb://<chunin1103>:<Neji1234!>@ds343895.mlab.com:43895/forecast-accuracy"

client = MongoClient(uri)
db = client.get_default_database()

# post_demo = db["Thoi_tiet"]

# "Thoi"