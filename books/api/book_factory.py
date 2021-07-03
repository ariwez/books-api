from typing import (
    Any,
    Dict,
    List,
)

from books.api.books_api_client import VolumesData
from books.book import Book

ItemData = Dict[str, Any]


class BookFactory:
    def create_many(
            self,
            volumes_data: VolumesData,
    ) -> List[Book]:
        items: List[ItemData] = volumes_data.get('items', {})
        books: List[Book] = [
            Book(
                item.get('id'),
                item.get('volumeInfo', {}).get('title'),
                item.get('volumeInfo', {}).get('authors'),
                item.get('volumeInfo', {}).get('publishedDate'),
                item.get('volumeInfo', {}).get('categories'),
                item.get('volumeInfo', {}).get('averageRating'),
                item.get('volumeInfo', {}).get('ratingsCount'),
                item.get('volumeInfo', {}).get('imageLinks', {}).get('thumbnail'),
            ) for item in items
        ]
        return books
