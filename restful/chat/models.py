from mongoengine import Document, StringField, DateTimeField, IntField


class ChatMessages(Document):
    date = DateTimeField()
    username = StringField(max_length=100)
    message = StringField(max_length=2000)
    message_id = IntField(max_value=1000000)
