__author__ = 'rrmerugu'

from pymongo import MongoClient
from datetime import datetime


def conn(dbname):
    db = MongoClient('mongodb://localhost')
    return db[dbname]


db = conn('chatter')

try:
    db.create_collection('chat_messages')
except Exception as e:
    print e


def read_file(file):
    return open(file, 'r').readlines()


def import_data(file, c):
    lines = read_file(file)
    print "Lines in chat %s is %s" % (file, len(lines))
    for l in lines:
        data = l.split(": ")
        # print data
        if len(data) >= 3:
            c = c + 1
            datum = {}
            datum['date'] = datetime.strptime(data[0], "%d-%m-%Y %H:%M:%S")
            datum['username'] = data[1]
            datum['message'] = data[2].rstrip('\n')
            datum['message_id'] = c
            print c
            db.chat_messages.insert(datum)


files = ['chat1.txt', 'chat2.txt', 'chat3.txt']

c = 1

for f in files:
    print "Reading %s" % f
    c = db.chat_messages.find().count()
    import_data('chats/%s' % f, c)
