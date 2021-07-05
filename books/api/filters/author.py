from typing import List

from django.db.models import QuerySet
from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request
from rest_framework.views import APIView


class AuthorFilter(BaseFilterBackend):
    def filter_queryset(
            self,
            request: Request,
            queryset: QuerySet,
            view: APIView,
    ) -> QuerySet:
        authors: List[str] = request.query_params.getlist("author")
        if authors:
            return queryset.filter(authors__overlap=authors)

        return queryset

    def get_schema_operation_parameters(self, view):
        return [
            {
                'name': 'author',
                'required': False,
                'in': 'query',
                'description': "Filter by author",
                'schema': {
                    'type': 'string',
                },
            },
        ]