from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db     = client.get_default_database()

posts = db["posts"]

post_list = posts.find()
post = {
    '''
<hr /> <strong>Ad </strong>
<p>👀👀👀👀👀👀 By <I>TA</i></p>
<p><strong style="font-size: 1.25em;"> Lose your virginity </strong> <em style="color: red; font-size: 1.5em;"> For free </em></p>

<p style="font: helvetica;">Come to 22C Th&agrave;nh C&ocirc;ng 😀</p>
<p>22:15 every Thursday night, (meet Mr. Huy or Mr. Quan)</p>
<i style="font-size: 0.8em">No question asked</i>

<hr />

    '''
}