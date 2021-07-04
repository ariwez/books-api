from django.urls import path

from books.api.views.book_details import BookDetailsView
from books.api.views.books_create import BooksCreateOrUpdateView
from books.api.views.books_list import BooksListView

urlpatterns = [
    path('books', BooksListView.as_view(), name="books_list"),
    path('books/<str:book_id>', BookDetailsView.as_view(), name="book_details"),
    path('db', BooksCreateOrUpdateView.as_view(), name="books_create_or_update"),
]