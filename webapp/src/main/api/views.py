from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from .serializers import AttributeNameSerializer, AttributeValueSerializer, AttributeSerializer
from ..models import AtributeName, AttributeValue, Attribute
from rest_framework.response import Response
from rest_framework.views import APIView


class AtributeNameAPIView(ReadOnlyModelViewSet):
    queryset = AtributeName.objects.all()
    serializer_class = AttributeNameSerializer

class AttributeValueAPIView(ReadOnlyModelViewSet):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer

class AttributeAPIView(ReadOnlyModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class ImportAPIView(APIView):
    def post(self, request):
        print("lol")
        return Response("lol")








