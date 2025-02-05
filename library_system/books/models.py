from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
