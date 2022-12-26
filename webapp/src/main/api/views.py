from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .serializers import AttributeNameSerializer, AttributeValueSerializer, AttributeSerializer, Serializer_class
from ..models import AttributeName, AttributeValue, Attribute
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

# AtributeName GET requests only
class AttributeNameAPIView(ReadOnlyModelViewSet):
    queryset = AttributeName.objects.all()
    serializer_class = AttributeNameSerializer

# AttributeValue GET requests only
class AttributeValueAPIView(ReadOnlyModelViewSet):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer

# Attribute GET requests only
class AttributeAPIView(ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer

class ImportAPIView(Serializer_class, APIView):
    def post(self, request):
        for i in request.data:
            key, value = list(i.items())[0]
            id = value.pop("id")

            serializer = self.serializer_class[key](data=value) #!!!! checking that the key exists, get()
            if not serializer.is_valid():
                return Response(
                    {
                        ValidationError(serializer.errors)
                    }
                )

            qveryset = self.serializer_class[key].Meta().model
            validData = serializer.validated_data
            serializer.save()
            # qveryset.objects.update_or_create(id=id, defaults=serializer.validated_data)
        
        return Response(
            {
                "message": "OK",
            }
        )
        







