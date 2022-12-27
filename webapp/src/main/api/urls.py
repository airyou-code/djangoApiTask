from django.urls import path
from rest_framework import routers
from .views import (
    AttributeNameAPIView, AttributeValueAPIView, AttributeAPIView,
    ProductAPIView, ProductAttributesAPIView, ProductImageAPIView,
    ImageAPIView, CatalogAPIView, ImportAPIView)

router = routers.DefaultRouter()
router.register(r'detail/AttributeName', AttributeNameAPIView, basename='AttributeName')
router.register(r'detail/AttributeValue', AttributeValueAPIView, basename='AttributeValue')
router.register(r'detail/Attribute', AttributeAPIView, basename='Attribute')
router.register(r'detail/Product', ProductAPIView, basename='Product')
router.register(r'detail/ProductAttributes', ProductAttributesAPIView, basename='ProductAttributes')
router.register(r'detail/ProductImage', ProductImageAPIView, basename='ProductImage')
router.register(r'detail/Image', ImageAPIView, basename='Image')
router.register(r'detail/Catalog', CatalogAPIView, basename='Catalog')
urlpatterns = [
    path('import/', ImportAPIView.as_view(), name='import'),
] + router.urls
