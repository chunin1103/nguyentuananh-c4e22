from pymongo import MongoClient
uri = "mongodb://chunin1103:Neji1234!@ds125293.mlab.com:25293/database_ini"

# Connect to database
client = MongoClient(uri)
db = client.get_default_database()

# Collection (chua cac ho so cung loai)
posts = db["posts"] # insert_one (C), find (R)

post_list = posts.find()

for p in post_list:
    print(p['title'])
    print(p['author'])
# Document (la cac ho so)

# # create a document

# post = {
#     'title': 'Hom nay troi xau vkl',
#     'content': 'Toi o nha @@3$%#',
#     'author': 'My dog, Mr. Wet Socks'
# }
# # # Insert documents into database
# # posts.insert_one(post)