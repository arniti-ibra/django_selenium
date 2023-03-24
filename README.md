# Run Website
1. create venv in root directory and pip install 
2. cd mysite
3. run `python manage.py runserver` --> click on link to see the website
4. open new terminal (dont close other one)
5. run `pytest` --> to run selenium tests

# Setup Process

1. In a Virtual environment, with Django in your requirements.txt
2. You're already ready, run `django-admin startproject mysite` (mac or win)

## Projects vs. Apps

What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website.

A project can contain multiple apps. An app can be in multiple projects.
3. there are two folders called mysite, you can rename the outer one as you wish - i chose the name `root`
4. cd root
5. python manage.py runserver  

## Automatic reloading of runserver

The development server automatically reloads Python code for each request as needed. You don’t need to restart the server for code changes to take effect. However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.

Your apps can live anywhere on your Python path. In this tutorial, we’ll create our poll app in the same directory as your manage.py file so that it can be imported as its own top-level module, rather than a submodule of mysite.
6. python manage.py startapp polls inside root folder, i.e. where `manage.py` is
7. You have now created a folder polls in the root folder. Here you can write your first view. I changed the text I expect to see in the view. But you have to call the view, you do that in django by mapping it to a URL. This requires URLconf in the polls directory.
8.  You make a urls.py file in the polls directory importing `path` from django.urls.
9.  Then you need to point the root URLconf at the polls.urls module (i.e. `urls.py` in root/mysite/urls.py)
You should always use `include()` when you include other URL patterns. admin.site.urls is the only exception to this.
10. python manage.py migrate
11. python manage.py runserver -> If you get an error page here, check that you’re going to http://localhost:8000/polls/ and not http://localhost:8000/.
You should get a website stating Hello, you've reached the polls index.

## Looking at path() in urls.py:

Takes 2 required arguments: **route** and **view**:

- ROUTE is a string that contains a URL pattern. When processing a request, Django starts at the first pattern in urlpatterns and makes its way down the list, comparing the requested URL against each pattern until it finds one that matches.
- Patterns don’t search GET and POST parameters, or the domain name. What that means is in the following 2 examples
  1. https://www.example.com/myapp/?page=3
  2. https://www.example.com/myapp/
   The URL conf looks for the same thing -> `myapp/.
- Given a matching pattern is found, it calls the specified view function with an HttpRequest object as the first argument and any “captured” values from the route as keyword arguments.
  
It also takes 2 optional requirements:

- path() argument: kwargs¶ 
  Arbitrary keyword arguments can be passed in a dictionary to the target view. We aren’t going to use this feature of Django in the tutorial.
- path() argument: name¶
  Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.


Changing Models:

1. Change your models (in models.py).
2. Run python manage.py makemigrations to create migrations for those changes
3. Run python manage.py migrate to apply those changes to the database.

python manage.py shell can be used to check and add to your database

Using Django Admin:

You need to create an Admin user w/password to determine who can log into admin site.

You can namespace in Django if you have many apps in one project
app_name = 'polls' in urls.py specific to the app (in this case polls)

## Connecting to SQL Proxy

1. SET USE_CLOUD_SQL_AUTH_PROXY=true
   This is what lets you run it in local, the code that enables this to happen can be seen in settings.py on line
