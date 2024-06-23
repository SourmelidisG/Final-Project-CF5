from django.test import TestCase
from .models import Author, Book

class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name='test_author_1', surname='test_author_1')
        Author.objects.create(name='test_author_2', surname='test_author_2')
        Author.objects.create(name='test_author_3', surname='test_author_3')

        Book.objects.create(title='The Big Book', subtitle='The Big Book subtitle', author=Author.objects.get(id=1), isbn='1234567890123', body='The Big Book body')
        Book.objects.create(title='The Small Book', subtitle='The Small Book subtitle', author=Author.objects.get(id=2), isbn='1234567890124', body='The Small Book body')
        Book.objects.create(title='The Medium Book', subtitle='The Medium Book subtitle', author=Author.objects.get(id=3), isbn='1234567890125', body='The Medium Book body')


    def test_access_books(self):
        book = Book.objects.get(id=1)
        self.assertEqual(book.title, 'The Big Book')
        self.assertEqual(book.subtitle, 'The Big Book subtitle')
        self.assertEqual(book.author, Author.objects.get(id=1))
        self.assertEqual(book.isbn, '1234567890123')
        self.assertEqual(book.body, 'The Big Book body')

    def test_access_authors(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.name, 'test_author_1')
        self.assertEqual(author.surname, 'test_author_1')

    def test_book_count(self):
        books = Book.objects.all()
        self.assertEqual(books.count(), 3)

    def test_author_count(self):
        authors = Author.objects.all()
        self.assertEqual(authors.count(), 3)



