import pymongo
import json
from datetime import datetime

client = pymongo.MongoClient("mongodb+srv://marczhu:123456a@cluster0.r6vhy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
coll = client.linedatabases.eventcollection


def dicMemberCheck(key, dicts):
    if key in dicts:
        return True
    else:
        return False


def write_to_data(data):
    coll.insert_one(data)


def get_body_info(body, line_bot_api):
    dicts = {}
    dict = json.loads(body)['events'][0]
    if dicMemberCheck('source', dict):
        if dicMemberCheck('userId', dict['source']):
            user_id = dict['source']['userId']
            if user_id:
                profile = line_bot_api.get_profile(user_id=str(user_id))
                if profile:
                    name = profile.display_name
                    if name:
                        dicts['name'] = name
    if dicMemberCheck('timestamp', dict):
        dicts['date'] = datetime.fromtimestamp(int(str(dict['timestamp'])[:10])).strftime("%Y-%m-%d, %H:%M:%S")
    dicts['events'] = dict
    return dicts




