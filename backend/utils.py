from typing import Optional

import httpx
from fastapi import HTTPException
from starlette import status

from config import settings
from enums import RequestType


async def send_httpx_request(url: str, request_type: RequestType, data: Optional[dict] = None, params: Optional[dict] = None):
    async with httpx.AsyncClient() as client:
        client.headers['Authorization'] = f'Bearer {settings.axenix_api_key}'
        print(f'{client.headers}\n\n')

        if request_type == RequestType.GET:
            response = await client.get(url, params=params)
            if response.status_code == 200:
                response_json = response.json()

                return response_json
            else:
                raise HTTPException(status_code=response.status_code)

        if request_type == RequestType.POST and data is not None:
            response = await client.post(url, data=data, params=params)

            if response.status_code == 200:
                response_json = response.json()

                return response_json
            else:
                raise HTTPException(status_code=response.status_code)
