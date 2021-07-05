from typing import Dict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.api.tests.response_data import details_response_data


class BookDetailsViewTest(APITestCase):
    fixtures = [
        'books.json',
    ]

    def test_missing_details(self) -> None:
        url = reverse("book_details", kwargs={'book_id': 'missing-book-id'})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        expected_response = {'detail': 'Not found.'}
        self.assertEqual(response.json(), expected_response)

    def test_book_details(self) -> None:
        book_id: str = 'ckD1DwAAQBAJ'

        url = reverse("book_details", kwargs={'book_id': book_id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(details_response_data))
        book_details_data: Dict = response.data
        expected_response_data: Dict = details_response_data
        self.assertEqual(book_details_data['book_id'], expected_response_data['book_id'])
        self.assertEqual(book_details_data['title'], expected_response_data['title'])
        self.assertEqual(book_details_data['authors'], expected_response_data['authors'])
        self.assertEqual(book_details_data['published_date'], expected_response_data['published_date'])
        self.assertEqual(book_details_data['categories'], expected_response_data['categories'])
        self.assertEqual(book_details_data['average_rating'], expected_response_data['average_rating'])
        self.assertEqual(book_details_data['ratings_count'], expected_response_data['ratings_count'])
        self.assertEqual(book_details_data['thumbnail'], expected_response_data['thumbnail'])
