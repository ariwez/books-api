from typing import Tuple

from django.db.models import QuerySet
from rest_framework.filters import (
    BaseFilterBackend,
    OrderingFilter,
)
from rest_framework.generics import (
    ListAPIView,
)

from books.api.filters.author import AuthorFilter
from books.api.filters.year import YearFilter
from books.api.models import Book
from books.api.serializers.book import BookSerializer


class BooksListView(ListAPIView):
    queryset: QuerySet = Book.objects.all()
    serializer_class: BookSerializer = BookSerializer
    filter_backends: Tuple[BaseFilterBackend] = (
        OrderingFilter,
        YearFilter,
        AuthorFilter,
    )
    ordering_fields: Tuple[str] = ('published_date',)
