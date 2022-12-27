from rest_framework import serializers
from ..models import (
    AttributeName, AttributeValue,Attribute,
    Product, ProductAttributes, ProductImage,
    Image, Catalog
)

class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeName
        fields = "__all__"

class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = "__all__"

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributes
        fields = "__all__"

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"

class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = "__all__"

        def update_create_MMF(self, id, validated_data):
            products = validated_data.pop("products_ids", None)
            attributes = validated_data.pop("attributes_ids", None)

            catalog = self.model.objects.update_or_create(id=id, defaults=validated_data)[0]
            if products:
                catalog.products_ids.clear()
                catalog.products_ids.add(*products)
            if attributes:
                catalog.attributes_ids.clear()
                catalog.attributes_ids.add(*attributes)

class Serializer_class:
    def __init__(self) -> None:
        self.get_serializer = {
            "AttributeName": AttributeNameSerializer,
            "AttributeValue": AttributeValueSerializer,
            "Attribute": AttributeSerializer,
            "Product": ProductSerializer,
            "ProductAttributes": ProductAttributesSerializer,
            "ProductImage": ProductImageSerializer,
            "Image": ImageSerializer,
            "Catalog": CatalogSerializer
        }
