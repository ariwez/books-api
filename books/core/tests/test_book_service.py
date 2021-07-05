from datetime import datetime
from typing import (
    List,
    Optional,
)
from unittest.mock import Mock

from django.test import TestCase

from books.api.models import Book
from books.core.book_service import BookService
from books.core.tests.api_client_response_data import volumes_data


class BookServiceTestCase(TestCase):
    def setUp(self) -> None:
        self.book_service = BookService()
        self.query: str = 'test-query'

    def test_empty_volumes_list(self) -> None:
        self.book_service.books_api_client.get_volumes_list_by_query = Mock(return_value={})

        result: int = self.book_service.get_and_save_books(self.query)

        expected_result: int = 0
        self.assertEqual(result, expected_result)
        self.assertEqual(Book.objects.count(), expected_result)

    def test_get_and_save_volumes_list(self) -> None:
        self.book_service.books_api_client.get_volumes_list_by_query = Mock(return_value=volumes_data)

        result: int = self.book_service.get_and_save_books(self.query)

        expected_result: int = 1
        self.assertEqual(result, expected_result)
        self.assertEqual(Book.objects.count(), expected_result)
        expected_book_id: str = "5WWeDwAAQBAJ"
        expected_title: str = "BITP 4/2019: Bezpieczeństwo i Technika Pożarnicza / Safety & Fire Technique"
        expected_authors: List[str] = ["st. bryg.  dr inż. Paweł Janik"]
        expected_published_date: datetime = datetime(2018, 12, 31)
        expected_categories: List[str] = ["Technology & Engineering"]
        expected_average_rating: Optional[float] = None
        expected_ratings_count: Optional[int] = None
        expected_thumbnail: str = "http://books.google.com/books/content?id=5WWeDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"

        self.assertIsNotNone(
            Book.objects.filter(
                book_id=expected_book_id,
                title=expected_title,
                authors=expected_authors,
                published_date=expected_published_date,
                categories=expected_categories,
                average_rating=expected_average_rating,
                ratings_count=expected_ratings_count,
                thumbnail=expected_thumbnail,
            ).first()
        )
