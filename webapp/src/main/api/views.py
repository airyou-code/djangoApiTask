from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet, ModelViewSet
from .serializers import AttributeNameSerializer, AttributeValueSerializer, AttributeSeritalizer, Serializer_class
from ..models import AttributeName, AttributeValue, Attribute
from rest_framework.response import Response
from rest_framework.views import APIView

# AtributeName GET requests only
class AttributeNameAPIView(ModelViewSet):
    queryset = AttributeName.objects.all()
    serializer_class = AttributeNameSerializer

# AttributeValue GET requests only
class AttributeValueAPIView(ReadOnlyModelViewSet):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer

# Attribute GET requests only
class AttributeAPIView(ReadOnlyModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSeritalizer


class ImportAPIView(Serializer_class, APIView):
    def post(self, request):
        json_data = request.data
        for i in json_data:
            *key, = i
            *value, = i.values()

            serializer = self.serializer_class[key[0]](data=value[0])
            serializer.is_valid(raise_exception=True)
            qveryset = self.serializer_class[key[0]].Meta().model

            self.create_update(qveryset, value[0])
        
        return Response(
            {
                "message": "OK",
            }
        )

    # def validater_m(self, key, data):
        







