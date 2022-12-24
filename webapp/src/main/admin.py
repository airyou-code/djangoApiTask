from django.contrib import admin
from .models import AtributeName, AttributeValue, Attribute

class AtributeNameAdmin(admin.ModelAdmin):
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


admin.site.register(AtributeName, AtributeNameAdmin)
admin.site.register(AttributeValue, AttributeValueAdmin)
admin.site.register(Attribute, AttributeAdmin)
