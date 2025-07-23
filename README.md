# Django 

Python Framework for backend. 

MVC : Model View Controller : to separeate the concerns : Model - data , View - html format that you view , Controller - Contorl this operation (This is root of all Backends)

in Django is MVT (Model View Template) : 

Django installation : 
sudo apt install python3-venv
python3 -m venv myenv
source ./myenv/bin/activate
python -m pip install django --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org
-  django-admin --version

- django-admin startproject learndjango : this will create a learndjango folder then again inside of this folder there will be : learndjango(repo)  manage.py(file) 
inside learndjango(repo) : __init__.py  asgi.py  settings.py  urls.py  wsgi.py (all are files)

This is how overall will look
projectname/ : here is where you start
├── manage.py
└── projectname/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

manage.py  that contains the actual project code :
 Commonly used commands:
  - python manage.py runserver (run the server)
  - python manage.py migrate
  - python manage.py startapp appname (to create app inside project(here we write our own codes))

__init__.py : Marks this directory as a Python package.
settings.py : Contains all the project’s settings and configuration.
urls.py : Contains the URL declarations for the project; the “table of contents” for the site’s URLs
wsgi.py :Stands for Web Server Gateway Interface.Used for deploying your project with WSGI-compatible servers (e.g., Gunicorn, uWSGI)

* A static application (or static website) delivers fixed content to the user. The content doesn’t change unless a developer manually updates the files.
* A dynamic application (or dynamic website) generates content on the fly, often based on user input, database queries, or other runtime logic.

- python manage.py startapp appname : 
__init__.py : Makes the appname folder a Python package. Required for Python to treat this directory as a module.
admin.py : Used to register models so they appear in the Django admin interface
apps.py : Contains a class (e.g., AppnameConfig) to configure the app. Django uses it for internal app management.
migrations/ : Stores database migration files for the app. __init__.py makes it a package. Django will put auto-generated migration files here (e.g., 0001_initial.py).
models.py : Where you define data models (classes that map to database tables).
tests.py : Contains test cases for your app using Django’s testing framework.
views.py : Contains view functions or class-based views that handle requests and return responses.


* LINKING
linking the project to an app is essential because it tells the project:
“Hey, this app exists and should be included in the overall configuration (like models, URLs, signals, etc.).
Step 1 : Add the App to INSTALLED_APPS -> inside settings.py of project :
'''INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ... default Django apps ...
    
    'appname',  # ✅ <-- Add your app here
]
'''
Step 2 : Include the App’s URLs
# projectname/urls.py (one time)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('yourapp/', include('appname.urls')),  # ✅ Include app's routes
] 

&& 
app has an urls.py file like:

# appname/urls.py (register the views here)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]


# appname/views.py (You create the views here)

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello World")


Why Keep Separate urls.py in Project and App?
- Separation of Concerns (Modularity)
Each app in Django is designed to be independent and reusable.
The project’s urls.py acts like the global router.
Each app’s urls.py defines routes related only to that app’s functionality.

- Reusability
Apps with their own urls.py can be reused in other projects with minimal changes.
Imagine a blog app:
It has models, views, templates, and its own urls.py.
You can plug it into any Django project by:
Adding it to INSTALLED_APPS
Including blog.urls in the main urls.py

Using templetes
Step 1 : Create `templetes` dir you can have html files here
Step 2 :  'DIRS': [BASE_DIR / 'templates']

if you follow this format :
 appname/
└── templates/
    └── appname/
        └── example.html

then in views
def home(request):
    context = {'message': 'Hello, Django!'}
    return render(request, 'appname/example.html', context)


* GET - fetching data from server - this will expose the values we are passing in the address bar
* POST - adding new data to server

Why Use POST Over GET?
1. POST is More Secure for Sensitive Data
GET exposes data in the URL (e.g., ?password=1234)

2. POST Supports Larger Payloads
GET requests have URL length limits (2KB–8KB, browser-dependent).
POST can handle large form submissions, file uploads, etc.

3. POST is Designed for "Write" Operations
By HTTP standards:
GET should be safe and idempotent (no side effects, doesn't change state)
POST is meant for actions that change data (create/update)

to specfiy <form method="get" action="/search">

MVT OR MTV : Model View Templete : In simple terms Data Logic :ayout

Static Files :
TO add all style and JS code you need to add static folder
Go to settings 
# settings.py

# URL to use when referring to static files located in STATICFILES_DIRS
STATIC_URL = '/static/'

# Optional: Additional locations the staticfiles app will traverse
STATICFILES_DIRS = [
    BASE_DIR / "static",  # for project-level static files
]

# Where to collect all static files for production (optional)
STATIC_ROOT = BASE_DIR / "staticfiles"

or 

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

use this in file {% load static %}
<link rel="stylesheet" href="{% static 'myapp/style.css' %}">
<img src="{% static 'myapp/logo.png' %}" alt="Logo">
<script src="{% static 'myapp/script.js' %}"></script>

for production collect all static files : python manage.py collectstatic
then run server

ORM : Object Relational Mapping
 in Django is a powerful feature that allows developers to interact with databases using Python code instead of writing raw SQL queries. It provides an abstraction layer between the application code and the database, making it easier to work with databases in a more object-oriented manner.

 What is ORM?
ORM is a technique that converts data between Python objects and database tables. Django’s ORM handles:

Creating tables
Inserting, updating, deleting rows
Running queries like filtering, sorting, joining, etc.

Go to Postgresql and create a new database : learningdjango
to connect to the database : go to settings.py -> In DATABASES, specify the database name, username, password, and other connection details. : 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'learningdjango',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
: pip install psycopg2

A normal class in models.py : file class Book(models.Model) should be like this to create a table in database 
after editing models.py run : python manage.py makemigrations (add appname.apps.AppConfig to INSTALLED_APPS in settings.py)
then run : python manage.py migrate

Need to install Pillow library : pip install Pillow (for images)

Admin Panel : Django provides a built-in admin interface that allows you to manage your data models easily. You can register your models with the admin site and customize the admin interface to suit your needs.
python manage.py createsuperuser
by registering the model in admin.py we can add, edit, delete data from admin panel.

Why MEDIA_ROOT and MEDIA_URL?
MEDIA_ROOT: This setting specifies the root directory where uploaded media files will be stored on the server. It's a directory path relative to the project's root directory.
MEDIA_URL: This setting defines the URL prefix for accessing the uploaded media files. It's a URL path that starts with a slash (/) and is used to construct the URL for accessing the media files.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')