from typing import (
    Any,
    Dict,
    Optional,
)
from parameterized import parameterized

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.api.tests.response_data import (
    published_date_2020,
    published_with_given_authors,
    sorted_by_published_date_ascending,
    sorted_by_published_date_descending,
    unordered_books_list,
    ResponseData,
)


class BooksListViewTest(APITestCase):
    fixtures = [
        'books.json',
    ]

    def test_empty_list(self) -> None:
        url = reverse("books_list")
        params = {'published_date': '2000'}

        response = self.client.get(url, params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_response = []
        self.assertEqual(response.json(), expected_response)

    @parameterized.expand([
        (None, unordered_books_list),
        ({'sort': '-published_date'}, sorted_by_published_date_descending),
        ({'sort': 'published_date'}, sorted_by_published_date_ascending),
        ({'published_date': '2020'}, published_date_2020),
        ({'author': ['Margaret Paton-Walsh', 'Brian Wicker']}, published_with_given_authors),
    ])
    def test_populated_list(
            self,
            params: Optional[Dict[str, Any]],
            expected_response_data: ResponseData,
    ) -> None:
        url = reverse("books_list")

        response = self.client.get(url, params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(expected_response_data))
        for index, book_data in enumerate(response.data):
            self.assertEqual(book_data['book_id'], expected_response_data[index]['book_id'])
            self.assertEqual(book_data['title'], expected_response_data[index]['title'])
            self.assertEqual(book_data['authors'], expected_response_data[index]['authors'])
            self.assertEqual(book_data['published_date'], expected_response_data[index]['published_date'])
            self.assertEqual(book_data['categories'], expected_response_data[index]['categories'])
            self.assertEqual(book_data['average_rating'], expected_response_data[index]['average_rating'])
            self.assertEqual(book_data['ratings_count'], expected_response_data[index]['ratings_count'])
            self.assertEqual(book_data['thumbnail'], expected_response_data[index]['thumbnail'])
