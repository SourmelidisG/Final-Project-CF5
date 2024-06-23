# books/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='authors/', null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    subtitle = models.CharField(max_length=250, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', null=True, blank=True)
    isbn = models.CharField(max_length=13,null=True, blank=True)
    body = models.TextField(null=True, blank=True, default='')
    def __str__(self):
        return self.title


