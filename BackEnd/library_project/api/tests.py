from django.test import TestCase
from books.models import Author, Book
from django.urls import reverse
class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name='test_author_1', surname='test_author_1')
        Author.objects.create(name='test_author_2', surname='test_author_2')
        Author.objects.create(name='test_author_3', surname='test_author_3')

        Book.objects.create(title='The Big Book', subtitle='The Big Book subtitle', author=Author.objects.get(id=1), isbn='1234567890123', body='The Big Book body')
        Book.objects.create(title='The Small Book', subtitle='The Small Book subtitle', author=Author.objects.get(id=2), isbn='1234567890124', body='The Small Book body')
        Book.objects.create(title='The Medium Book', subtitle='The Medium Book subtitle', author=Author.objects.get(id=3), isbn='1234567890125', body='The Medium Book body')

    def test_api_books(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)

    def test_api_authors(self):
        response = self.client.get(reverse('author_list'))
        self.assertEqual(response.status_code, 200)

    def test_api_books_retrive(self):
        response = self.client.get(reverse('book_retrive', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_api_authors_retrive(self):
        response = self.client.get(reverse('author_retrive', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_api_books_info(self):
        response = self.client.get(reverse('book_retrive', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Big Book')
        self.assertContains(response, 'The Big Book subtitle')
        self.assertContains(response, 'The Big Book body')

