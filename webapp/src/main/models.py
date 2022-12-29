from django.db import models

class AttributeName(models.Model):
    nazev = models.CharField(max_length=200, null=True, blank=True)
    kod = models.CharField(max_length=200, null=True, blank=True)
    zobrazit = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}: {self.nazev}"

class AttributeValue(models.Model):
    hodnota = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return f"{self.id}: {self.hodnota}"

class Attribute(models.Model):
    nazev_atributu_id  = models.ForeignKey(AttributeName, on_delete=models.DO_NOTHING, blank=True, null=True)
    hodnota_atributu_id =  models.ForeignKey(AttributeValue, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.id}: {self.nazev_atributu_id.nazev}, {self.hodnota_atributu_id.hodnota}"

class Product(models.Model):
    nazev = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    cena = models.IntegerField(blank=True, null=True)
    mena = models.CharField(max_length=3, blank=True)
    published_on = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(null=True, blank=True)
    def __str__(self):
        return f"{self.id}: {self.nazev[:20]}"

class ProductAttributes(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, blank=True, null=True)

class Image(models.Model):
    nazev = models.CharField(max_length=200, blank=True, null=True)
    obrazek = models.URLField(max_length=2000, blank=True, null=True)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, blank=True, null=True)
    obrazek_id = models.ForeignKey(Image, on_delete=models.DO_NOTHING, blank=True, null=True)
    nazev = models.CharField(max_length=200, blank=True, null=True)

class Catalog(models.Model):
    nazev = models.CharField(max_length=200, blank=True, null=True)
    obrazek_id = models.ForeignKey(Image, on_delete=models.DO_NOTHING, blank=True, null=True)
    products_ids = models.ManyToManyField(Product, blank=True)
    attributes_ids = models.ManyToManyField(Attribute, blank=True)