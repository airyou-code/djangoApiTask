from rest_framework import serializers
from ..models import AtributeName, AttributeValue, Attribute

class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtributeName
        fields = "__all__"

class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = "__all__"

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = "__all__"


class Serializer_class:
    def __init__(self):
        self.serializer_class = {
            "Attribute": AttributeNameSerializer,
            "AttributeValue": AttributeValueSerializer,
            "AttributeName": AttributeNameSerializer
        }
