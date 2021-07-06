from datetime import datetime, date
from typing import Optional

from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError
from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request
from rest_framework.views import APIView


class YearFilter(BaseFilterBackend):
    def filter_queryset(
            self,
            request: Request,
            queryset: QuerySet,
            view: APIView,
    ) -> QuerySet:
        year: Optional[str] = request.query_params.get("published_date")
        if year is None:
            return queryset

        if not year.isnumeric():
            raise ValidationError(f"Value should be numeric, instead {year} was passed.")

        return queryset.filter(published_date__year=int(year))

    def get_schema_operation_parameters(self, view):
        return [
            {
                'name': 'published_date',
                'required': False,
                'in': 'query',
                'description': "Filter by year, expects: \"YYYY\"",
                'schema': {
                    'type': 'string',
                },
            },
        ]