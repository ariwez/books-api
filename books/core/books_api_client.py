import os
from typing import Dict, NoReturn, Any

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from books.config.settings import GOOGLE_DEVELOPER_KEY

VolumesData = Dict[str, Any]
SERVICE_NAME = 'books'
SERVICE_VERSION = 'v1'


class BooksApiClient:
    def __init__(
            self,
            service_name: str = SERVICE_NAME,
            service_version: str = SERVICE_VERSION,
            developer_key: str = GOOGLE_DEVELOPER_KEY,
    ) -> NoReturn:
        self.service_name = service_name
        self.service_version = service_version
        self.developer_key = developer_key

    def get_volumes_list_by_query(
            self,
            query: str,
    ) -> VolumesData:
        with build(self.service_name, self.service_version, developerKey=self.developer_key) as service:
            response: VolumesData = {}
            try:
                response = service.volumes().list(q=query).execute()
            except HttpError as e:
                print(f'Error response status code : {e.status_code}, reason : {e.error_details}')

        return response
