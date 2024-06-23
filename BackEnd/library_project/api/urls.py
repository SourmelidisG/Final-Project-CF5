from django.urls import path


from .views import BookAPIView, BookRetriveApiView
from .views import AuthorAPIView, AuthorRetriveApiView
urlpatterns = [
    path('book', BookAPIView.as_view(), name='book_list'),
    path('book/<int:pk>', BookRetriveApiView.as_view(), name='book_retrive'),
    path('author', AuthorAPIView.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorRetriveApiView.as_view(), name='author_retrive'),

]
