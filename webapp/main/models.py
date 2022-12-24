from django.db import models

class AtributeName(models.Model):
    nazev = models.CharField(max_length=200, default="")
    kod = models.CharField(max_length=200, default="")

class AttributeValue(models.Model):
    hodnota = models.CharField(max_length=200, default="")

class Attribute(models.Model):
    nazev_atributu_id  = models.ForeignKey(AtributeName, on_delete=models.DO_NOTHING)
    hodnota_atributu_id =  models.ForeignKey(AttributeValue, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.id}: {self.nazev_atributu_id.nazev}, {self.hodnota_atributu_id.hodnota}"
