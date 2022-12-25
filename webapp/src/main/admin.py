from django.contrib import admin
from .models import AttributeName, AttributeValue, Attribute

class AttributeNameAdmin(admin.ModelAdmin):
    list_display = ["id", "nazev"]
    search_fields = ["id", "nazev"]
    list_filter  = ["id"]

class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ["id", "hodnota"]
    search_fields = ["id", "hodnota"]
    list_filter  = ["id"]

class AttributeAdmin(admin.ModelAdmin):
    search_fields = ["id", "nazev_atributu_id", "hodnota_atributu_id"]
    list_filter  = ["id"]


admin.site.register(AttributeName, AttributeNameAdmin)
admin.site.register(AttributeValue, AttributeValueAdmin)
admin.site.register(Attribute, AttributeAdmin)
