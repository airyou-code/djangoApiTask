from django.contrib import admin
from .models import (
    AttributeName, AttributeValue, Attribute,
    Product, ProductAttributes, ProductImage,
    Image, Catalog
)

class AttributeNameAdmin(admin.ModelAdmin):
    list_display = ["id", "nazev"]
    search_fields = ["id", "nazev"]
    list_filter  = ["id", "nazev"]

class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ["id", "hodnota"]
    search_fields = ["id", "hodnota"]
    list_filter  = ["id"]

class AttributeAdmin(admin.ModelAdmin):
    list_display = ["id", "nazev_atributu_id", "hodnota_atributu_id"]
    search_fields = ["id", "nazev_atributu_id", "hodnota_atributu_id"]
    list_filter  = ["id"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "nazev", "cena", "mena", "is_published"]
    search_fields = ["id", "nazev", "cena", "mena", "is_published"]
    list_filter = ["id", "cena", "published_on", "nazev"]

class ProductAttributesAdmin(admin.ModelAdmin):
    list_display = ["id", "attribute", "product"]
    search_fields = ["id"]
    list_filter = ["id"]

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ["id", "nazev", "product"]
    search_fields = ["id", "nazev"]
    list_filter = ["id", "nazev"]

class ImageAdmin(admin.ModelAdmin):
    list_display = ["id", "nazev"]
    search_fields = ["id", "nazev"]
    list_filter = ["id", "nazev"]

class CatalogAdmin(admin.ModelAdmin):
    list_display = ["id", "nazev"]
    search_fields = ["id", "nazev_atributu_id", "hodnota_atributu_id"]
    list_filter = ["id"]



admin.site.register(AttributeName, AttributeNameAdmin)
admin.site.register(AttributeValue, AttributeValueAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttributes, ProductAttributesAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Catalog, CatalogAdmin)
