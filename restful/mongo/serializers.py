import mongoengine
from django.db import models
from django.forms import widgets
from rest_framework import fields
from rest_framework_mongoengine import serializers
from rest_framework_mongoengine.fields import ReferenceField, ListField, EmbeddedDocumentField, DynamicField
#from restful.mongo.fields import IDField



#MongoEngineModelSerializer is now DocumentSerializer - in serializers.py of monogengine
class MongoModelSerializer(serializers.DocumentSerializer):

    def get_field(self, model_field):
        kwargs = {}

        if model_field.__class__ in (mongoengine.ReferenceField, mongoengine.EmbeddedDocumentField,
                                     mongoengine.ListField, mongoengine.DynamicField):
            kwargs['model_field'] = model_field
            kwargs['depth'] = self.opts.depth

        if not model_field.__class__ == mongoengine.ObjectIdField:
            kwargs['required'] = model_field.required

        if model_field.__class__ == mongoengine.EmbeddedDocumentField:
            kwargs['document_type'] = model_field.document_type

        if model_field.default:
            kwargs['required'] = False
            kwargs['default'] = model_field.default

        if model_field.__class__ == models.TextField:
            kwargs['widget'] = widgets.Textarea

        field_mapping = {
            mongoengine.FloatField: fields.FloatField,
            mongoengine.IntField: fields.IntegerField,
           # mongoengine.DateTimeField: DateTimeLocaleField,
            mongoengine.EmailField: fields.EmailField,
            mongoengine.URLField: fields.URLField,
            mongoengine.StringField: fields.CharField,
            mongoengine.BooleanField: fields.BooleanField,
            mongoengine.FileField: fields.FileField,
            mongoengine.ImageField: fields.ImageField,
            mongoengine.ObjectIdField: fields.Field,
            mongoengine.ReferenceField: ReferenceField,
            mongoengine.ListField: ListField,
            mongoengine.EmbeddedDocumentField: EmbeddedDocumentField,
            mongoengine.DynamicField: DynamicField,
            mongoengine.DecimalField: fields.DecimalField,
            mongoengine.SequenceField: fields.IntegerField,
           # IDField: fields.IntegerField
        }

        attribute_dict = {
            mongoengine.StringField: ['max_length'],
            mongoengine.DecimalField: ['min_value', 'max_value'],
            mongoengine.EmailField: ['max_length'],
            mongoengine.FileField: ['max_length'],
            mongoengine.ImageField: ['max_length'],
            mongoengine.URLField: ['max_length'],
        }

        if model_field.__class__ in attribute_dict:
            attributes = attribute_dict[model_field.__class__]
            for attribute in attributes:
                kwargs.update({attribute: getattr(model_field, attribute)})

        try:
            return field_mapping[model_field.__class__](**kwargs)
        except KeyError:
            return fields.ModelField(model_field=model_field, **kwargs)
