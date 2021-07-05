from typing import (
    Any,
    Dict,
    List,
)

ResponseData = List[Dict[str, Any]]

unordered_books_list: ResponseData = [
    {
        "book_id": "NCJnAAAAMAAJ",
        "title": "Our War Too",
        "authors": [
            "Margaret Paton-Walsh"
        ],
        "published_date": "2002-01-01",
        "categories": [
            "History"
        ],
        "average_rating": None,
        "ratings_count": None,
        "thumbnail": "http://books.google.com/books/content?id=NCJnAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
        "created_at": "2021-07-04T14:57:16.158386Z",
        "updated_at": "2021-07-04T14:57:16.158420Z"
    },
    {
        "book_id": "OEnZAAAAMAAJ",
        "title": "Studying War--no More?",
        "authors": [
            "Brian Wicker"
        ],
        "published_date": "1994-01-01",
        "categories": [
            "Religion"
        ],
        "average_rating": None,
        "ratings_count": None,
        "thumbnail": "http://books.google.com/books/content?id=OEnZAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
        "created_at": "2021-07-04T14:57:16.162292Z",
        "updated_at": "2021-07-04T14:57:16.162313Z"
    },
    {
        "book_id": "ckD1DwAAQBAJ",
        "title": "China’s Good War",
        "authors": [
            "Rana Mitter"
        ],
        "published_date": "2020-09-15",
        "categories": [
            "History"
        ],
        "average_rating": 4.0,
        "ratings_count": 1,
        "thumbnail": "http://books.google.com/books/content?id=ckD1DwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
        "created_at": "2021-07-04T14:57:16.164238Z",
        "updated_at": "2021-07-04T14:57:16.164250Z"
    }
]

sorted_by_published_date_descending: ResponseData = [
    {
        "book_id": "ckD1DwAAQBAJ",
        "title": "China’s Good War",
        "authors": [
            "Rana Mitter"
        ],
        "published_date": "2020-09-15",
        "categories": [
            "History"
        ],
        "average_rating": 4,
        "ratings_count": 1,
        "thumbnail": "http://books.google.com/books/content?id=ckD1DwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
        "created_at": "2021-07-04T14:57:16.164238Z",
        "updated_at": "2021-07-04T14:57:16.164250Z"
    },
    {
        "book_id": "NCJnAAAAMAAJ",
        "title": "Our War Too",
        "authors": [
            "Margaret Paton-Walsh"
        ],
        "published_date": "2002-01-01",
        "categories": [
            "History"
        ],
        "average_rating": None,
        "ratings_count": None,
        "thumbnail": "http://books.google.com/books/content?id=NCJnAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
        "created_at": "2021-07-04T14:57:16.158386Z",
        "updated_at": "2021-07-04T14:57:16.158420Z"
    },
    {
        "book_id": "OEnZAAAAMAAJ",
        "title": "Studying War--no More?",
        "authors": [
            "Brian Wicker"
        ],
        "published_date": "1994-01-01",
        "categories": [
            "Religion"
        ],
        "average_rating": None,
        "ratings_count": None,
        "thumbnail": "http://books.google.com/books/content?id=OEnZAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
        "created_at": "2021-07-04T14:57:16.162292Z",
        "updated_at": "2021-07-04T14:57:16.162313Z"
    }
]

sorted_by_published_date_ascending: ResponseData = [
    {
        "book_id": "OEnZAAAAMAAJ",
        "title": "Studying War--no More?",
        "authors": [
            "Brian Wicker"
        ],
        "published_date": "1994-01-01",
        "categories": [
            "Religion"
        ],
        "average_rating": None,
        "ratings_count": None,
        "thumbnail": "http://books.google.com/books/content?id=OEnZAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
        "created_at": "2021-07-04T14:57:16.162292Z",
        "updated_at": "2021-07-04T14:57:16.162313Z"
    },
    {
        "book_id": "NCJnAAAAMAAJ",
        "title": "Our War Too",
        "authors": [
            "Margaret Paton-Walsh"
        ],
        "published_date": "2002-01-01",
        "categories": [
            "History"
        ],
        "average_rating": None,
        "ratings_count": None,
        "thumbnail": "http://books.google.com/books/content?id=NCJnAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
        "created_at": "2021-07-04T14:57:16.158386Z",
        "updated_at": "2021-07-04T14:57:16.158420Z"
    },
    {
        "book_id": "ckD1DwAAQBAJ",
        "title": "China’s Good War",
        "authors": [
            "Rana Mitter"
        ],
        "published_date": "2020-09-15",
        "categories": [
            "History"
        ],
        "average_rating": 4,
        "ratings_count": 1,
        "thumbnail": "http://books.google.com/books/content?id=ckD1DwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
        "created_at": "2021-07-04T14:57:16.164238Z",
        "updated_at": "2021-07-04T14:57:16.164250Z"
    }
]

published_date_2020: ResponseData = [
    {
        "book_id": "ckD1DwAAQBAJ",
        "title": "China’s Good War",
        "authors": [
            "Rana Mitter"
        ],
        "published_date": "2020-09-15",
        "categories": [
            "History"
        ],
        "average_rating": 4,
        "ratings_count": 1,
        "thumbnail": "http://books.google.com/books/content?id=ckD1DwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
        "created_at": "2021-07-04T14:57:16.164238Z",
        "updated_at": "2021-07-04T14:57:16.164250Z"
    }
]

published_with_given_authors: ResponseData = [
    {
        "book_id": "NCJnAAAAMAAJ",
        "title": "Our War Too",
        "authors": [
            "Margaret Paton-Walsh"
        ],
        "published_date": "2002-01-01",
        "categories": [
            "History"
        ],
        "average_rating": None,
        "ratings_count": None,
        "thumbnail": "http://books.google.com/books/content?id=NCJnAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
        "created_at": "2021-07-04T14:57:16.158386Z",
        "updated_at": "2021-07-04T14:57:16.158420Z"
    },
    {
        "book_id": "OEnZAAAAMAAJ",
        "title": "Studying War--no More?",
        "authors": [
            "Brian Wicker"
        ],
        "published_date": "1994-01-01",
        "categories": [
            "Religion"
        ],
        "average_rating": None,
        "ratings_count": None,
        "thumbnail": "http://books.google.com/books/content?id=OEnZAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
        "created_at": "2021-07-04T14:57:16.162292Z",
        "updated_at": "2021-07-04T14:57:16.162313Z"
    }
]

details_response_data: Dict[str, Any] = {
  "book_id": "ckD1DwAAQBAJ",
  "title": "China’s Good War",
  "authors": ["Rana Mitter"],
  "published_date": "2020-09-15",
  "categories": ["History"],
  "average_rating": 4.0,
  "ratings_count": 1,
  "thumbnail": "http://books.google.com/books/content?id=ckD1DwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
  "created_at": "2021-07-04T14:57:16.164238Z",
  "updated_at": "2021-07-04T14:57:16.164250Z"
}