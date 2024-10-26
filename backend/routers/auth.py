import httpx
from fastapi import APIRouter, HTTPException
from starlette import status

from backend.config import settings
from backend.enums import RequestType
from backend.schemas.auth import Token, RegisterInfo, LoginInfo
from backend.utils import send_httpx_request

router = APIRouter(prefix='auth', tags=['Аутентификация'])


@router.post('/register', response_model=Token)
async def register(reg_info: RegisterInfo):
    reg_info = reg_info.dict(exclude_unset=True)
    reg_info['team'] = settings.team_name

    return await send_httpx_request(f'{settings.case_api_url}/register',
                                    request_type=RequestType.POST,
                                    json=reg_info)


@router.post('/login', response_model=Token)
async def login(login_info: LoginInfo):
    login_info = login_info.dict(exclude_unset=True)

    return await send_httpx_request(f'{settings.case_api_url}/login',
                                    request_type=RequestType.POST,
                                    json=login_info)


# todo: бля авторизация пользователя не нужна ливаем, ну тогда просто получаем токен и потом его юзаем