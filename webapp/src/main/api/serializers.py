from rest_framework import serializers
from ..models import AttributeName, AttributeValue, Attribute

class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeName
        fields = "__all__"

class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = "__all__"

class AttributeSeritalizer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = "__all__"


class Serializer_class:
    def __init__(self):
        self.serializer_class = {
            "AttributeName": AttributeNameSerializer,
            "AttributeValue": AttributeValueSerializer,
            "Attribute": AttributeSerializer
        }

    def create_update(self, qveryset, data):
        model = qveryset.objects.filter(id=data["id"])
        if model:
            data.pop("id")
            a = model.update(**data)
            print(a)
        else:
            a = qveryset.objects.create(**data)
            print(a) 
        pass
