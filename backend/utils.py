from typing import Optional

import httpx
from fastapi import HTTPException, Depends
from starlette import status

from backend.auth import get_auth_headers, oauth2_password_bearer_scheme
from backend.enums import RequestType


async def send_httpx_request(url: str, request_type: RequestType, token: str = Depends(oauth2_password_bearer_scheme), data: Optional[dict] = None):
    async with httpx.AsyncClient() as client:
        client.headers['bearerAuth'] = token
        if request_type == RequestType.GET:
            response = await client.get(url)
            response_json = response.json()

            if response_json.get('error'):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response_json['error'])

            return response_json
        if request_type == RequestType.POST and data is not None:
            response = await client.post(url, data=data)
            response_json = response.json()

            if response_json.get('error'):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response_json['error'])

            return response_json
