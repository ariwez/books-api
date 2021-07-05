from typing import (
    Any,
    Dict,
    List,
)

from books.core.books_api_client import VolumesData
from books.core.book import Book

ItemData = Dict[str, Any]
VOLUME_INFO_KEY = 'volumeInfo'


class BookFactory:
    def create_many(
            self,
            volumes_data: VolumesData,
    ) -> List[Book]:
        items: List[ItemData] = volumes_data.get('items', {})
        books: List[Book] = [
            Book(
                item.get('id'),
                item.get(VOLUME_INFO_KEY, {}).get('title'),
                item.get(VOLUME_INFO_KEY, {}).get('authors'),
                item.get(VOLUME_INFO_KEY, {}).get('publishedDate'),
                item.get(VOLUME_INFO_KEY, {}).get('categories'),
                item.get(VOLUME_INFO_KEY, {}).get('averageRating'),
                item.get(VOLUME_INFO_KEY, {}).get('ratingsCount'),
                item.get(VOLUME_INFO_KEY, {}).get('imageLinks', {}).get('thumbnail'),
            ) for item in items
        ]
        return books
