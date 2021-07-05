from typing import Optional, List

from django.http import JsonResponse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from books.core.book_service import BookService


class BooksCreateOrUpdateView(APIView):
    authentication_classes: List = []

    def post(
            self,
            request: Request,
    ) -> JsonResponse:
        query: Optional[str] = request.data.get('q')
        if not query:
            return JsonResponse(data={'error': 'Invalid query param'}, status=status.HTTP_400_BAD_REQUEST)

        books_count: int = BookService().get_and_save_books(query)
        return JsonResponse(data={'books_count': books_count}, status=status.HTTP_201_CREATED)
