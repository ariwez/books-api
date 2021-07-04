from dataclasses import dataclass
from typing import (
    List,
    Optional,
    Union,
)


@dataclass
class Book:
    id: str
    title: str
    authors: List[str]
    published_date: str
    categories: List[str]
    average_rating: Optional[Union[float, int]]
    ratings_count: Optional[int]
    thumbnail: str
