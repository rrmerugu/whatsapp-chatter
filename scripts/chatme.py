__author__ = 'rrmerugu'

from pymongo import MongoClient
import re
from datetime import datetime


def conn(dbname):
    db = MongoClient('mongodb://localhost')
    return db[dbname]


db = conn('chatter')

BUFFER_SIZE = 5

kw = "love|luv|lv"


def get_the_buffer_data(message_id):
    print message_id
    ids = []

    for id in range(message_id - BUFFER_SIZE, message_id + BUFFER_SIZE + 1):
        ids.append(id)

    return ids


def get_the_message(message_id):
    print message_id
    message = ""
    try:
        message = db.chat_messages.find_one({'message_id': message_id})
    except Exception as e:
        message = "NA"
    return message


query = db.chat_messages.find({'message': re.compile(kw)})
for d in query:
    print d['message_id']
    buffer_of_messages = get_the_buffer_data(d['message_id'])
    for message_id in buffer_of_messages:
        print get_the_message(message_id)['message']

    print "================================="

print query.count()
