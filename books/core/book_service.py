from datetime import (
    date,
    datetime,
)
from typing import List, Optional

from django.utils import timezone

from books.core.book_factory import BookFactory
from books.core.books_api_client import (
    BooksApiClient,
    VolumesData,
)
from books.core.book import Book as BookData
from books.api.models import Book

DEFAULT_MONTH = 1
DEFAULT_DAY = 1


class BookService:
    def __init__(self):
        self.books_api_client: BooksApiClient = BooksApiClient()
        self.book_factory: BookFactory = BookFactory()

    def get_and_save_books(
            self,
            query: str,
    ) -> int:
        volumes_data: VolumesData = self.books_api_client.get_volumes_list_by_query(query)
        books: List[BookData] = self.book_factory.create_many(volumes_data)

        books_to_save: List[Book] = [
            Book(
                book_id=book.id,
                title=book.title,
                authors=book.authors,
                published_date=self.get_published_date_from_string(book.published_date),
                categories=book.categories,
                average_rating=book.average_rating,
                ratings_count=book.ratings_count,
                thumbnail=book.thumbnail,
                updated_at=timezone.now(),
            ) for book in books
        ]

        Book.objects.bulk_update_or_create(
            books_to_save,
            [
                'title',
                'authors',
                'published_date',
                'categories',
                'average_rating',
                'ratings_count',
                'thumbnail',
                'updated_at',
            ],
            match_field='book_id',
        )

        return len(books_to_save)

    def get_published_date_from_string(
            self,
            published_date: Optional[str],
    ) -> Optional[date]:
        if not published_date:
            return None

        sections: List[str] = published_date.split('-')
        if not sections:
            return None

        year: Optional[int] = int(sections[0])
        month: int = int(sections[1]) if len(sections) >= 2 else DEFAULT_MONTH
        day: int = int(sections[2]) if len(sections) == 3 else DEFAULT_DAY
        return datetime(year, month, day)
