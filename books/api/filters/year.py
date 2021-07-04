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
        if not year.isnumeric():
            raise ValidationError(f"Value should be numeric, instead {year} was passed.")

        date_from: date = datetime(int(year), 1, 1)
        date_to: date = datetime(int(year), 12, 31)

        return queryset.filter(published_date__gte=date_from, published_date__lte=date_to)
