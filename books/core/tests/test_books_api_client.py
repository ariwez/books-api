from unittest import mock

from django.test import TestCase

from books.core.books_api_client import VolumesData, BooksApiClient
from books.core.tests.api_client_response_data import volumes_data


class BooksApiClientTestCase(TestCase):
    def setUp(self) -> None:
        self.books_api_client = BooksApiClient()

    def test_empty_response(self) -> None:
        empty_response: VolumesData = {}
        query: str = "test-query"

        with mock.patch(
                'books.core.books_api_client.BooksApiClient.get_volumes_list_by_query',
                return_value=empty_response,
        ):
            result = self.books_api_client.get_volumes_list_by_query(query)

        expected_result: VolumesData = {}
        self.assertEqual(result, expected_result)

    def test_valid_response(self) -> None:
        response: VolumesData = volumes_data
        query: str = "test-query"

        with mock.patch(
                'books.core.books_api_client.BooksApiClient.get_volumes_list_by_query',
                return_value=response,
        ):
            result = self.books_api_client.get_volumes_list_by_query(query)

        expected_result: VolumesData = volumes_data
        self.assertEqual(result, expected_result)
