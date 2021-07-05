from django.db.models import QuerySet
from rest_framework.generics import (
    get_object_or_404,
    RetrieveAPIView,
)

from books.api.models import Book
from books.api.serializers.book import BookSerializer


class BookDetailsView(RetrieveAPIView):
    """
    Returns details of a book with given book_id.
    """
    queryset: QuerySet = Book.objects.all()
    serializer_class: BookSerializer = BookSerializer

    def get_object(self):
        queryset: QuerySet = self.filter_queryset(self.get_queryset())
        book: Book = get_object_or_404(queryset, book_id=self.kwargs.get('book_id'))
        return book
