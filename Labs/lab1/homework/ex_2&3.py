from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"


client = MongoClient(uri)
db = client.get_default_database()

posts = db["posts"] 

post = {
    'title': 'Because everybody loves cats',
    'content': '''──────▄▀▄─────▄▀▄
─────▄█░░▀▀▀▀▀░░█▄
─▄▄──█░░░░░░░░░░░█──▄▄
█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█

───▄▄─▄████▄▐▄▄▄▌
──▐──████▀███▄█▄▌
▐─▌──█▀▌──▐▀▌▀█▀
─▀───▌─▌──▐─▌
─────█─█──▐▌█
''',
    'author': 'Must hide my name because if this fails, man, I"ll be so Quê'
}


posts.insert_one(post)