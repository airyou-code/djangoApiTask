from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .serializers import (
    AttributeNameSerializer, AttributeValueSerializer, AttributeSerializer,
    ProductSerializer, ProductAttributesSerializer, ProductImageSerializer,
    ImageSerializer, CatalogSerializer, Serializer_class
)

from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  status

# AtributeName [GET] requests only
class AttributeNameAPIView(ReadOnlyModelViewSet):
    queryset = AttributeNameSerializer.Meta().model.objects.all()
    serializer_class = AttributeNameSerializer

# AttributeValue [GET] requests only
class AttributeValueAPIView(ReadOnlyModelViewSet):
    queryset = AttributeValueSerializer.Meta().model.objects.all()
    serializer_class = AttributeValueSerializer

# Attribute [GET] requests only
class AttributeAPIView(ReadOnlyModelViewSet):
    queryset = AttributeSerializer.Meta().model.objects.all()
    serializer_class = AttributeSerializer

# Product [GET] requests only
class ProductAPIView(ReadOnlyModelViewSet):
    queryset = ProductSerializer.Meta().model.objects.all()
    serializer_class = ProductSerializer

# ProductAttributes [GET] requests only
class ProductAttributesAPIView(ReadOnlyModelViewSet):
    queryset = ProductAttributesSerializer.Meta().model.objects.all()
    serializer_class = ProductAttributesSerializer

# ProductImage [GET] requests only
class ProductImageAPIView(ReadOnlyModelViewSet):
    queryset = ProductImageSerializer.Meta().model.objects.all()
    serializer_class = ProductImageSerializer

# Image [GET] requests only
class ImageAPIView(ReadOnlyModelViewSet):
    queryset = ImageSerializer.Meta().model.objects.all()
    serializer_class = ImageSerializer

# Catalog [GET] requests only
class CatalogAPIView(ReadOnlyModelViewSet):
    queryset = CatalogSerializer.Meta().model.objects.all()
    serializer_class = CatalogSerializer

# Import [POST] requests only
class ImportAPIView(Serializer_class, APIView):
    """ Endpoint for all models

    Args:
        APIView (_type_): post

    Returns:
        str: status message
        code: status code
    """
    def error_handler(self, message="Invalid input data type", error_code=status.HTTP_400_BAD_REQUEST):
        self.error = {"message": message, "status": error_code}

    def post(self, request):
        
        self.error_handler()
        if type(request.data) == list:
            for i in request.data:
                if type(i) != dict:
                    self.error_handler("Invalid input data type, expected 'dict'", status.HTTP_400_BAD_REQUEST)
                    break
                key, value = list(i.items())[0]
                id = value.pop("id", None)

                serializer_class = self.get_serializer.get(key)
                if not serializer_class:
                    self.error_handler(f"Model '{key}' not found")
                    break

                serializer = serializer_class(data=value)
                if not serializer.is_valid():
                    self.error_handler(ValidationError(serializer.errors))
                    break

                if not id:
                    serializer.save()
                    self.error_handler("Ok", status.HTTP_201_CREATED)
                    continue

                model = self.get_serializer[key].Meta().model
                try:
                    model.objects.update_or_create(id=id, defaults=serializer.validated_data)
                except TypeError:
                    serializer_class.Meta().update_create_MMF(id, serializer.validated_data)

                except Exception as e:
                    self.error_handler(ValidationError(e))

                self.error_handler("Ok", status.HTTP_201_CREATED)

        return Response(
            {
                "message": self.error["message"],
            }, status=self.error["status"],
        )







