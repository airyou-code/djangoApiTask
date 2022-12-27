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
   "ModelName": {
      "id": 1, 
      "column1": "data",
      "column2": "data"
   }  
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
