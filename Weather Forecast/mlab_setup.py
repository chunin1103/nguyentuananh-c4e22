import mongoengine

# "mongodb://<chunin1103>:<Neji1234!>@ds343895.mlab.com:43895/forecast-accuracy"
host        = 'ds343895.mlab.com'
port        = '24778'
db_name        = 'forecast-accuracy'
user_name        = 'chunin1103'
password        = 'Neji1234!'

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(1):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())
    