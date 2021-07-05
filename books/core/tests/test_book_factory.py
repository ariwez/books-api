from typing import List

from django.test import TestCase

from books.core.book import Book
from books.core.book_factory import BookFactory
from books.core.books_api_client import VolumesData
from books.core.tests.api_client_response_data import volumes_data


class BookFactoryTestCase(TestCase):
    def setUp(self) -> None:
        self.book_factory = BookFactory()

    def test_empty_volumes_list(self) -> None:
        empty_volumes: VolumesData = {}

        result: List[Book] = self.book_factory.create_many(empty_volumes)

        expected_result: List[Book] = []
        self.assertEqual(result, expected_result)

    def test_creating_list_from_volumes(self) -> None:
        volumes: VolumesData = volumes_data

        result: List[Book] = self.book_factory.create_many(volumes)

        expected_result: List[Book] = [Book(
            "5WWeDwAAQBAJ",
            "BITP 4/2019: Bezpieczeństwo i Technika Pożarnicza / Safety & Fire Technique",
            ["st. bryg.  dr inż. Paweł Janik"],
            "2018-12-31",
            ["Technology & Engineering"],
            None,
            None,
            "http://books.google.com/books/content?id=5WWeDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
        )]

        self.assertEqual(result, expected_result)
