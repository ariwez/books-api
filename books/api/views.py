from dataclasses import asdict
from typing import Dict, List

from django.http import HttpRequest, JsonResponse

from books.api.book_service import BookService


def books(request: HttpRequest) -> JsonResponse:
    books_list: List[Dict] = [asdict(book) for book in BookService().get_and_save_books('hobbit')]
    return JsonResponse(books_list, safe=False)
