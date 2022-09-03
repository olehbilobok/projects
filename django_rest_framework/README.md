Description:

There are two python projects which work together. 

"domria_parser_all project" scraps https://dom.ria.com/ website and send data to the PostgreSQL using Django ORM. In this project two methods were implemented:

1) HEAD, which checks presence of data into the database
2) POST, which writes data into the database in case of its absence.

In "django_rest project" CRUD operations were implemented which allow to write, read, update, delete data. Except basic CRUD operations this project allows to make selection via filter parameters and of course pagination, login and logout were implemented.  

Run Project(commands):

1)open "django_rest project"
2)virtualenv vent -p python3
3)source venv/bin/activate
4)pip install -r requirements.txt
5)In this project I use postgreSQL that's why you should change credentials in settings and create database  
6)python manage.py makemigrations
7)python manage.py migrate
8)python manage.py runserver
9)open "domria_parser_all project"
10)choose apartments.py file
11)virtualenv venv -p python3
12)source venv/bin/activate
13)pip install -r requirements.txt
14)python appartments.py