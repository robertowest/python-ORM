import sys

try:
    from django.db import models
except  Exception:
    print("Hubo un error al cargar los módulos de django. ¿Tiene django instalado?")
    sys.exit()


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=60, default="")
    state_province = models.CharField(max_length=30, default="")
    country = models.CharField(max_length=50, default="")
    website = models.URLField()
    class Meta:
        db_table = "publisher"
    def __str__(self):
        return self.name


class Author(models.Model):
    salutation = models.CharField(max_length=10, default="")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    class Meta:
        db_table = "author"
    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    class Meta:
        db_table = "book"
    def __str__(self):
        return self.title
