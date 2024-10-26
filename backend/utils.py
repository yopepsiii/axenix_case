from typing import Optional

import httpx
from fastapi import HTTPException
from starlette import status

from backend.enums import RequestType


async def send_httpx_request(url: str, request_type: RequestType, json: Optional[dict] = None):
    async with httpx.AsyncClient() as client:
        if request_type == RequestType.GET:
            response = await client.get(url)
            response_json = response.json()

            if response_json.get('error'):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response_json['error'])

            return response_json
        if request_type == RequestType.POST and json is not None:
            response = await client.post(url, json=json)
            response_json = response.json()

            if response_json.get('error'):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response_json['error'])

            return response_json
