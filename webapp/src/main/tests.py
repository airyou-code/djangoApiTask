from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json
from .models import (
    AttributeName, AttributeValue, Attribute,
    Product, ProductAttributes, ProductImage,
    Image, Catalog
)

class ImportTestCase(APITestCase):
    def setUp(self):
        pass

    def test_create_defaultModel(self):
        data =[ {
            "AttributeName": {
                "id": 1,
                "nazev": "Barva"
            }
        }]
        response = self.client.post(reverse("import"), data, format='json')
        self.assertAlmostEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertAlmostEqual(AttributeName.objects.get(id=1).nazev, "Barva")

    def test_update_defaultModel(self):
        data = [
            {
                "AttributeName": {
                    "id": 1,
                    "nazev": "Barva"
                }
            },
            {
                "AttributeName": {
                    "id": 1,
                    "nazev": "modrá"
                }
            }
        ]
        response = self.client.post(reverse("import"), data, format='json')
        self.assertAlmostEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertAlmostEqual(AttributeName.objects.get().nazev, "modrá")

    def test_create_ModelWithForeignKey_notExistForeignKey(self):
        data = [
            {
                "AttributeName": {
                    "id": 1,
                    "nazev": "Barva"
                }
            },
            {
                "AttributeValue": {
                    "id": 1,
                    "hodnota": "modrá"
                }
            },
            {
                "Attribute": {
                    "id": 1,
                    "nazev_atributu_id": 1,
                    "hodnota_atributu_id": 1
                }
            }
        ]
        response = self.client.post(reverse("import"), data, format='json')
        self.assertAlmostEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertAlmostEqual(AttributeName.objects.get().nazev_atributu_id.nazev, "Barva")
        self.assertAlmostEqual(AttributeName.objects.get().hodnota_atributu_id.hodnota, "modrá")


    def test_create_ModelWithForeignKey_notExistForeignKey(self):
        data = [
            {
                "Attribute": {
                    "id": 1,
                    "nazev_atributu_id": 1,
                    "hodnota_atributu_id": 1
                }
            }
        ]
        response = self.client.post(reverse("import"), data, format='json')
        self.assertAlmostEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_data(self):
        with open('test_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            response = self.client.post(reverse("import"), data, format='json')
            self.assertAlmostEqual(response.status_code, status.HTTP_201_CREATED)


