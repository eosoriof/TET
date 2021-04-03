import pymongo
import json

connection_string = """
mongodb+srv://middleware:ksShpi9xS4XFGBaN@middlewaredb.zwxw2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
""".strip()
client = pymongo.MongoClient(connection_string)
db = client['middleware']
queue_table = db['queues']  # collection/table
user_table = db['users']


def register_queue(queue_name, owner_name):
    queue = {'queue_name': queue_name,
             'owner_name': owner_name
             }
    if queue_table.find_one({'queue_name': queue_name}):
        return None #queue alreadye exists
    res = queue_table.insert_one(queue)
    queue_id = res.inserted_id
    return queue_id


def get_queues():
    queues = queue_table.find()
    queue_list = [q for q in queues]
    for q in queue_list:
        del q['_id']
    return queue_list


def erase_queue(queue_name, owner_name):
    queue = {'queue_name': queue_name,
             'owner_name': owner_name
             }
    #if queue_table.find_one(queue):
    x = queue_table.delete_one(queue)
    return x.deleted_count


def register_user(username, password):
    user = {'username': username,
            'password': password
            }
    if user_table.find_one(user):
        return None # User already exists
    res = user_table.insert_one(user)
    user_id = res.inserted_id
    return user_id


def login_user(username, password):
    query = {'username': username,
             'password': password
             }
    user = user_table.find_one(query)
    if not user:
        return None
    return {'username': username}
