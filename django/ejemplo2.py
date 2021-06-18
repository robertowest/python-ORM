#!/usr/bin/env python

# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Your application specific imports
from data.models import *


# el siguiente código ejecutará tres consultas (todos los libros y el editor por cada libro)
# SELECT "book"."id", "book"."title", "book"."publisher_id", "book"."publication_date" FROM "book"; args=()
# SELECT "publisher"."id", "publisher"."name", "publisher"."address", "publisher"."city", "publisher"."state_province", "publisher"."country", "publisher"."website" FROM "publisher" WHERE "publisher"."id" = 1 LIMIT 21; args=(1,)
# SELECT "publisher"."id", "publisher"."name", "publisher"."address", "publisher"."city", "publisher"."state_province", "publisher"."country", "publisher"."website" FROM "publisher" WHERE "publisher"."id" = 1 LIMIT 21; args=(1,)
books = Book.objects.all()
for obj in books:
    print( obj.title, obj.publisher )


# el siguiente código ejecutará una consultas (todos los libros con todos sus editores)
# SELECT "book"."id", "book"."title", "book"."publisher_id", "book"."publication_date", "publisher"."id", "publisher"."name", "publisher"."address", "publisher"."city", "publisher"."state_province", "publisher"."country", "publisher"."website" FROM "book" LEFT OUTER JOIN "publisher" ON ("book"."publisher_id" = "publisher"."id"); args=()
books = Book.objects.all().select_related("publisher")
for obj in books:
    print( obj.title, obj.publisher )


# en caso de relación many-to-many utilizaremos prefetch_related
# el siguiente código ejecutará dos consultas (todos los libros y todos los autores de los libros seleccionados)
# SELECT "book"."id", "book"."title", "book"."publisher_id", "book"."publication_date" FROM "book"; args=()
# SELECT ("book_authors"."book_id") AS "_prefetch_related_val_book_id", "author"."id", "author"."salutation", "author"."first_name", "author"."last_name", "author"."email" FROM "author" INNER JOIN "book_authors" ON ("author"."id" = "book_authors"."author_id") WHERE "book_authors"."book_id" IN (1, 2); args=(1, 2)
books = Book.objects.all().prefetch_related("authors")
for obj in books:
    print( obj.title, obj.authors.all() )


# mejorando las queries
# evitar de traer datos innecesarios
# si solo necesitamos el título del libro y el nombre del editor, prodríamos realizar la query
# Book.objects.all().select_related("publisher").values('title', 'publisher_name')
