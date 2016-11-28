'''
import pytz
from datetime import datetime
from mongoengine.connection import get_db
from mongoengine.fields import SequenceField #,DateTimeField

class IDField(SequenceField):

    def generate(self):
        """
        Generate and Increment the counter
        """
        sequence_name = self.get_sequence_name()
        sequence_id = "%s.%s" % (sequence_name, self.name)
        collection = get_db(alias=self.db_alias)[self.collection_name]
        data = collection.find_one({"_id": sequence_id})
        if data:
            counter = collection.find_and_modify(query={"_id": sequence_id}, update={"$inc": {"next": 1}}, new=True, upsert=True)
        else:
            counter = {"_id": sequence_id, "next": 1000}
            collection.insert(counter)
        return self.value_decorator(counter['next'])
'''