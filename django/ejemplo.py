#!/usr/bin/env python

# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Your application specific imports
from data.models import *


def create_publisher():
    # creamos una publicación
    p = Publisher()
    p.name = 'O REILLY'
    p.address = '898  Bell Street'
    p.city = 'New York'
    p.state_province = 'New York'
    p.country = 'EEUU'
    p.website = 'https://www.learnpython.org/es/'
    p.save()


def create_author():
    # creamos un autor
    a = Author()
    a.first_name = 'Mark'
    a.last_name = 'Lutz'
    a.salutation = 'Sr.'
    a.save()


def create_books(authors, publisher):
    # creamos un libro con autores y editor
    b1 = Book()
    b1.title = "Learning Python: Powerful Object-Oriented Programming"
    b1.publisher = publisher
    b1.publication_date = '2013-09-07'
    b1.save()
    # agregamos los autores
    for obj in authors:
        b1.authors.add(obj)
    b1.save()
    # creamos otro libro (satos mínimos)
    b2 = Book()
    b2.title = 'Python Pocket Reference: Python in Your Pocket'
    b2.publisher = publisher
    b2.publication_date = '2014-02-11'
    b2.save()


def queries():
    books = Book.objects.all()
    for obj in books:
        print( obj.title, obj.publisher )
        
    books = Book.objects.all().select_related("publisher")
    for obj in books:
        print( obj.title, obj.publisher )    


if __name__ == "__main__":
    create_publisher()
    publisher = Publisher.objects.get(id=1)
    create_author()
    authors = Author.objects.filter(id=1)
    create_books(authors, publisher)
