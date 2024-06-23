from rest_framework import serializers
from books.models import Book, Author

class BookSerializer(serializers.ModelSerializer):


    class Meta:
        model = Book
        fields = ('pk', 'title', 'subtitle', 'author',  'isbn', 'body')
        read_only_fields = ('pk',)
        depth = 1

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('pk', 'name', 'surname', 'image')
        read_only_fields = ('pk',)