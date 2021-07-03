from typing import List

from books.api.book_factory import BookFactory
from books.api.books_api_client import (
    BooksApiClient,
    VolumesData,
)
from books.book import Book


class BookService:
    def __init__(self):
        self.books_api_client: BooksApiClient = BooksApiClient()
        self.book_factory: BookFactory = BookFactory()

    def get_and_save_volumes(
            self,
            query: str,
    ):
        volumes_data: VolumesData = self.books_api_client.get_volumes_list_by_query(query)
        books: List[Book] = self.book_factory.create_many(volumes_data)
        return books
