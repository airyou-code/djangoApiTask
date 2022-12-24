from django.urls import path
from rest_framework import routers
from .views import AtributeNameAPIView, AttributeValueAPIView, AttributeAPIView, ImportAPIView

router = routers.DefaultRouter()
router.register(r'detail/AttributeName', AtributeNameAPIView, basename='AttributeName')
router.register(r'detail/AttributeValue', AttributeValueAPIView, basename='AttributeValue')
router.register(r'detail/Attribute', AttributeAPIView, basename='Attribute')

print(router.urls)

urlpatterns = [
    path('import/', ImportAPIView.as_view(), name='import'),
] + router.urls
