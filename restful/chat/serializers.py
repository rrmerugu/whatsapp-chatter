__author__ = 'rrmerugu'

from restful.mongo.serializers import MongoModelSerializer
from restful.chat.models import ChatMessages


class ChatMessagesSerializer(MongoModelSerializer):
    class Meta:
        model = ChatMessages
        lookup_field = "message_id"
        fields = ("message", "message_id", "username", "date")
