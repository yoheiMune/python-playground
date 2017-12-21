# Django Sample.

## Requirements.
Python3.x

## Install Django.
[reference](https://docs.djangoproject.com/en/2.0/intro/install/)  
```
# Install.
$ pip3 install Django
```
```
# Check the version.
$ python3 -m django --version
2.0
```

## How to get started.
[reference](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)  
### Create a project.
Create a project named `myroom`.
```
$ django-admin startproject myroom
```
Check the result.
```
$ tree myroom/
myroom/
├── manage.py
└── myroom
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```
Go into the project.
```
$ cd myroom
```
### The development server.
```
$ python3 manage.py runserver

# Or,
$ django-admin runserver --settings=myroom.settings --pythonpath="."

# for local
# $ django-admin runserver --settings=myroom.settings_local --pythonpath="."
```
Then, access.
```
http://127.0.0.1:8000/
```

## Create an app.
[reference](https://docs.djangoproject.com/en/2.0/intro/tutorial01/#creating-the-polls-app)  
Create an app named `polls`.
```
$ python3 manage.py startapp polls
```
Check the result.
```
$ tree polls
polls
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

## Let's implement your code.
[reference](https://docs.djangoproject.com/en/2.0/intro/tutorial01/#write-your-first-view)

## References.
* [https://www.djangoproject.com/](https://www.djangoproject.com/)
