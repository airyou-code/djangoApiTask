<h1>DjangoApiTask</h1>
API-REST that will accept and analyze a specific JSON data format

## Stack technology
- Django
- RestAPI

## Project launch

          $ pip install -r webapp/requirements.txt 
          $ python webapp/src/manage.py makemigrations
          $ python webapp/src/manage.py migrate
          $ python webapp/src/manage.py runserver

To create an **superuser account**, use this command:

          $ python webapp/src/manage.py createsuperuser

to run tests:
          
          $ python webapp/src/manage.py test main

## API logic

### Import

```http
POST http://127.0.0.1:8000/import/ + json
```
 
 - if 'id' is not specified, a new record will be created in the table whis new id
 - if 'id' is specified and exists in table, then change the existing row, if not, then create a new one with the specified id
 
 json format(each model has its own data structure):
 
```json
[
   "ModelName1": {
      "id": 1, 
      "column1": "data",
      "column2": "data"
   }, 
   "ModelName1": {
      "id": 1, 
      "column1": [1,2,3]
   },
]
```

json exempl:
```json
   "Catalog": {
      "id": 1,
      "nazev": "Výprodej 2018",
      "obrazek_id": 4,
      "products_ids": [
         "product.id",
         "..."
      ],
      "attributes_ids": [
         "attribute.id",
         "..."
      ]
   }
```

### Detail

format:
```http
GET http://127.0.0.1:8000/detail/ModelName
GET http://127.0.0.1:8000/detail/ModelName/idModel
```

json exempl:
```http
GET http://127.0.0.1:8000/detail/Catalog
GET http://127.0.0.1:8000/detail/Catalog/1
```

## Project expansion
It is possible to add new models, for this you need to create a serializer of this model

and add the serializer to the get_serializer list 

path **webapp/src/main/api/serializers.py**

```python
class Serializer_class:
    def __init__(self) -> None:
        self.get_serializer = {
            "AttributeName": AttributeNameSerializer,
            "AttributeValue": AttributeValueSerializer,
            "Attribute": AttributeSerializer,
            "Product": ProductSerializer,
            "ProductAttributes": ProductAttributesSerializer,
            "ProductImage": ProductImageSerializer,
            "Image": ImageSerializer,
            "Catalog": CatalogSerializer,
            "NewModel": NewModelSerializer #NewModel
        }
```

## Project file structure

```bash
.
├── test_data.json
└── webapp
    ├── requirements.txt
    └── src
        ├── main
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── api
        │   │   ├── serializers.py
        │   │   ├── urls.py
        │   │   └── views.py
        │   ├── apps.py
        │   ├── migrations
        │   │   └── __init__.py
        │   ├── models.py
        │   ├── tests.py
        │   └── views.py
        ├── manage.py
        └── webapp
            ├── __init__.py
            ├── asgi.py
            ├── settings.py
            ├── urls.py
            └── wsgi.py
```
