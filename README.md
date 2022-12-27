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









## Project file structure

```
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
        │   │   ├── 0001_initial.py
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
