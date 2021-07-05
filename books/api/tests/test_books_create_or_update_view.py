from unittest import mock

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class BooksCreateOrUpdateViewTest(APITestCase):
    def test_invalid_query(self) -> None:
        url = reverse("books_create_or_update")

        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected_response = {'error': 'Invalid query param'}
        self.assertEqual(response.json(), expected_response)

    def test_valid_create(self) -> None:
        url = reverse("books_create_or_update")
        query_data = {'q': 'test-query'}
        expected_result: int = 10

        with mock.patch('books.core.book_service.BookService.get_and_save_books', return_value=expected_result):
            response = self.client.post(url, query_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_response = {'books_count': expected_result}
        self.assertEqual(response.json(), expected_response)
