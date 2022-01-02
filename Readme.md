# Project to integrate react and django framework

### frontend: React
### backend: Django



# Setup the project
### install conda
### pip install django djangorestframework



# Useful command for django
## Start a project
### django-admin startproject xxx
### exp: django-admin startproject music_controller

## Start a app
### django-admin startapp xxx

## Update Database
### python ./manage.py makemigrations
### python ./manage.py migrate

## Start a server
### python manage.py runserver

## clear database
### python manage.py flush


# Useful command for react/npm

### 1. npm init -y

# Useful operation
### 1. add app under project, under settings.py INSTALLED_APPS field, add the app you added
### Structure of pwd
```bash
├── api
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── frontend
│   ├── admin.py
│   ├── apps.py
│   ├── babel.config.json
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── node_modules
│   ├── package.json
│   ├── package-lock.json
│   ├── __pycache__
│   ├── Readme.md
│   ├── src
│   ├── static
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── webpack.config.js
├── manage.py
└── music_controller
    ├── asgi.py
    ├── __init__.py
    ├── __pycache__
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```